import numpy as np
import matplotlib.pyplot as plt
import json
from math import sqrt, pow, pi
import time

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError:
    import Image
    import ImageDraw
    import ImageOps

class Vector( object ):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, b):
        return self.x*b.x + self.y*b.y + self.z*b.z

    def cross(self, b):
        return (self.y*b.z-self.z*b.y, self.z*b.x-self.x*b.z, self.x*b.y-self.y*b.x)

    def magnitude(self):
        return sqrt(self.x**2+self.y**2+self.z**2)

    def normal(self):
        mag = self.magnitude()
        return Vector(self.x/mag,self.y/mag,self.z/mag)

    def __add__(self, b):
        return Vector(self.x + b.x, self.y+b.y, self.z+b.z)

    def __sub__(self, b):
        return Vector(self.x-b.x, self.y-b.y, self.z-b.z)

    def __mul__(self, b):
        assert type(b) == float or type(b) == int
        return Vector(self.x*b, self.y*b, self.z*b)     

class Sphere( object ):

    def __init__(self, center, radius, color):
        self.c = center
        self.r = radius
        self.col = color

    def intersection(self, l):
        q = l.d.dot(l.o - self.c)**2 - (l.o - self.c).dot(l.o - self.c) + self.r**2
        if q < 0:
            return Intersection( Vector(0,0,0), -1, Vector(0,0,0), self)
        else:
            d = -l.d.dot(l.o - self.c)
            d1 = d - sqrt(q)
            d2 = d + sqrt(q)
            if 0 < d1 and ( d1 < d2 or d2 < 0):
                return Intersection(l.o+l.d*d1, d1, self.normal(l.o+l.d*d1), self)
            elif 0 < d2 and ( d2 < d1 or d1 < 0):
                return Intersection(l.o+l.d*d2, d2, self.normal(l.o+l.d*d2), self)
            else:
                return Intersection( Vector(0,0,0), -1, Vector(0,0,0), self)    

    def normal(self, b):
        return (b - self.c).normal()

class Cylinder( object ):
    def __init__(self, startpoint, endpoint, radius, color):
        self.s = startpoint
        self.e = endpoint
        self.r = radius
        self.col = color

    def intersection(self, l):
        q = l.d.dot(l.o - self.c)**2 - (l.o - self.c).dot(l.o - self.c) + self.r**2
        if q < 0:
            return Intersection( Vector(0,0,0), -1, Vector(0,0,0), self)
        else:
            d = -l.d.dot(l.o - self.c)
            d1 = d - sqrt(q)
            d2 = d + sqrt(q)
            if 0 < d1 and ( d1 < d2 or d2 < 0):
                return Intersection(l.o+l.d*d1, d1, self.normal(l.o+l.d*d1), self)
            elif 0 < d2 and ( d2 < d1 or d1 < 0):
                return Intersection(l.o+l.d*d2, d2, self.normal(l.o+l.d*d2), self)
            else:
                return Intersection( Vector(0,0,0), -1, Vector(0,0,0), self)    

    def normal(self, b):
        return (b - self.c).normal()

class LightBulb( Sphere ):
        pass

class Plane( object ):
    def __init__(self, point, normal, color):
        self.n = normal
        self.p = point
        self.col = color

    def intersection(self, l):
        d = l.d.dot(self.n)
        if d == 0:
            return Intersection( vector(0,0,0), -1, vector(0,0,0), self)
        else:
            d = (self.p - l.o).dot(self.n) / d
            return Intersection(l.o+l.d*d, d, self.n, self)

class Rectangle( object ):
    "not done. like a plane, but is limited to the shape of a defined rectangle"
    def __init__(self, point, normal, color):
        self.n = normal
        self.p = point
        self.col = color

    def intersection(self, ray):
        desti = ray.dest.dot(self.n)
        if desti == 0:
                        #??
            return Intersection( vector(0,0,0), -1, vector(0,0,0), self)
        else:
            desti = (self.p - ray.orig).dot(self.n) / desti
            return Intersection(ray.orig+ray.desti*desti, desti, self.n, self)

class RectangleBox( object ):

        pass

class AnimatedObject( object ):

        def __init__(self, *objs):
                self.objs = objs

        def __iter__(self):
                for obj in self.objs:
                        yield obj

        def __getitem__(self, index):
                return self.objs[index]

        def reverse(self):
                self.objs = [each for each in reversed(self.objs)]
                return self

#RAY TRACING INTERNAL COMPONENTS
class Ray( object ):

    def __init__(self, origin, direction):
        self.o = origin
        self.d = direction

class Intersection( object ):

    def __init__(self, point, distance, normal, obj):
        self.p = point
        self.d = distance
        self.n = normal
        self.obj = obj

def testRay(ray, objects, ignore=None):
    intersect = Intersection( Vector(0,0,0), -1, Vector(0,0,0), None)

    for obj in objects:
        if obj is not ignore:
            currentIntersect = obj.intersection(ray)
            if currentIntersect.d > 0 and intersect.d < 0:
                intersect = currentIntersect
            elif 0 < currentIntersect.d < intersect.d:
                intersect = currentIntersect
    return intersect

def trace(ray, objects, light, maxRecur):
    if maxRecur < 0:
        return (0,0,0)
    intersect = testRay(ray, objects)       
    if intersect.d == -1:
        col = vector(AMBIENT,AMBIENT,AMBIENT)
    elif intersect.n.dot(light - intersect.p) < 0:
        col = intersect.obj.col * AMBIENT
    else:
        lightRay = Ray(intersect.p, (light-intersect.p).normal())
        if testRay(lightRay, objects, intersect.obj).d == -1:
            lightIntensity = 1000.0/(4*pi*(light-intersect.p).magnitude()**2)
            col = intersect.obj.col * max(intersect.n.normal().dot((light - intersect.p).normal()*lightIntensity), AMBIENT)
        else:
            col = intersect.obj.col * AMBIENT
    return col

def gammaCorrection(color,factor):
    return (int(pow(color.x/255.0,factor)*255),
            int(pow(color.y/255.0,factor)*255),
            int(pow(color.z/255.0,factor)*255))

#USER FUNCTIONS
class Camera:

    def __init__(self, cameraPos, zoom=50.0, xangle=-5, yangle=-5):
        self.pos = cameraPos
        self.zoom = zoom
        self.xangle = xangle
        self.yangle = yangle

def renderScene(camera, lightSource, objs, imagedims, savepath):
        imgwidth,imgheight = imagedims
        img = PIL.Image.new("RGB",imagedims)
        #objs.append( LightBulb(lightSource, 0.2, Vector(*white)) )
        print "rendering 3D scene"
        t=time.clock()
        for x in xrange(imgwidth):
                #print x
                for y in xrange(imgheight):
                        ray = Ray( camera.pos, (Vector(x/camera.zoom+camera.xangle,y/camera.zoom+camera.yangle,0)-camera.pos).normal())
                        col = trace(ray, objs, lightSource, 10)
                        img.putpixel((x,imgheight-1-y),gammaCorrection(col,GAMMA_CORRECTION))
        print "time taken", time.clock()-t
        img.save(savepath)

def renderAnimation(camera, lightSource, staticobjs, animobjs, imagedims, savepath, saveformat):
        "savepath should not have file extension, but saveformat should have a dot"
        time = 0
        while True:
                print "time",time
                timesavepath = savepath+"_"+str(time)+saveformat
                objs = []
                objs.extend(staticobjs)
                objs.extend([animobj[time] for animobj in animobjs])
                renderScene(camera, lightSource, objs, imagedims, timesavepath)
                time += 1

        ## first stage - normalization
        def normalize(vector):
            return vector / np.linalg.norm(vector)

        ##intersection of the sphere figure
        def sphere_intersect(center, radius, ray_origin, ray_direction):
            b = 2 * np.dot(ray_direction, ray_origin - center)
        c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        return None
    ##another scope for AStriangle figures
    def ray_intersect_triangle(p0, p1, triangle):
        v0, v1, v2 = triangle
        u = v1 - v0
        v = v2 - v0
        normal = np.cross(u, v)
        b = np.inner(normal, p1 - p0)
        a = np.inner(normal, v0 - p0)
        
        if (b == 0.0):
            if a != 0.0:
                # ray is outside but parallel to the plane
                return 0
            else:
                # ray is parallel and lies in the plane
                rI = 0.0
        else:
            rI = a / b
        if rI < 0.0:
            return 0
        w = p0 + rI * (p1 - p0) - v0
        denom = np.inner(u, v) * np.inner(u, v) - \
            np.inner(u, u) * np.inner(v, v)
        si = (np.inner(u, v) * np.inner(w, v) - \
            np.inner(v, v) * np.inner(w, u)) / denom
        if (si < 0.0) | (si > 1.0):
            return 0
        ti = (np.inner(u, v) * np.inner(w, u) - \
            np.inner(u, u) * np.inner(w, v)) / denom
        if (ti < 0.0) | (si + ti > 1.0):
            return 0
        if (rI == 0.0):
            return 2
        return 1
    def nearest_intersected_object(objects, ray_origin, ray_direction)://supersempling
        distances = [sphere_intersect(obj['center'], obj['radius'], ray_origin, ray_direction) for obj in objects]
        nearest_object = None
        min_distance = np.inf
        for index, distance in enumerate(distances):
            if distance and distance < min_distance:
                min_distance = distance
                nearest_object = objects[index]
        return nearest_object, min_distance



    #supersampling usage
    def redrawAutograph(json_string, height=SIGNATURE_HEIGHT, width=SIGNATURE_WIDTH, im_border_size=IMAGE_BORDER_SIZE,
                        im_border_fill=IMAGE_BORDER_FILL):
        try:
            drawing = json.loads(json_string)
        except Exception, e:
            raise Exception(e.args)
        else:
            im = Image.new("RGBA", (width*RESIZE, height*RESIZE), "#FFF")
            draw = ImageDraw.Draw(im)
            try:
                for line in drawing['lines']:
                    draw.line(list(tuple([point[0]*RESIZE, point[1]*RESIZE]) for point in line),
                              fill="#000", width=RESIZE*2)
            except Exception, e:
                raise Exception(e.args)
            finally:
                del draw
            im = ImageOps.expand(im, border=im_border_size, fill=im_border_fill)
            im.thumbnail((width, height), Image.ANTIALIAS)
            return im

# example for testing

# For SuperSampling
#RESIZE = 5 
#IMAGE_BORDER_SIZE = RESIZE
#IMAGE_BORDER_FILL = "#A0A0A0"
#SIGNATURE_WIDTH = 400
#SIGNATURE_HEIGHT = 200
#json_string = {"lines":[[[84.5,34],[84.5,35],[84.5,37],[85.5,41],[86.5,50],[87.5,59],[89.5,68],[89.5,79],[89.5,85],[90.5,90],[90.5,92]],[[193.5,25],[193.5,26],[194.5,26],[194.5,32],[195.5,41],[197.5,46],[198.5,55],[200.5,64],[202.5,74],[204.5,80],[207.5,87],[207.5,91],[208.5,91]],[[142.5,59],[142.5,60],[142.5,61],[142.5,62],[142.5,66],[141.5,74],[138.5,81],[137.5,90],[134.5,97],[134.5,102],[134.5,106],[134.5,107],[134.5,109],[134.5,110],[136.5,110],[137.5,112],[139.5,112],[142.5,114],[147.5,116],[149.5,117],[150.5,117]],[[112.5,129],[112.5,130],[112.5,131],[114.5,131],[115.5,134],[120.5,139],[127.5,143],[134.5,150],[142.5,157],[150.5,163],[159.5,168],[161.5,170],[163.5,171],[164.5,171],[165.5,171],[169.5,168],[173.5,163],[177.5,156],[183.5,149],[186.5,142],[188.5,134],[188.5,128],[188.5,124],[188.5,121],[188.5,120]]]}

#width = 300
#height = 200

#camera = np.array([0, 0, 1])
#ratio = float(width) / height
#screen = (-1, 1 / ratio, 1, -1 / ratio) # left, top, right, bottom

#objects = [
#    { 'center': np.array([-0.2, 0, -1]), 'radius': 0.7 },
#    { 'center': np.array([0.1, -0.3, 0]), 'radius': 0.1 },
#    { 'center': np.array([-0.3, 0, 0]), 'radius': 0.15 }
#]

#image = np.zeros((height, width, 3))
#for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
#    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
#        pixel = np.array([x, y, 0])
#        origin = camera
#        direction = normalize(pixel - origin)
#
#        # check for intersections
#        nearest_object, min_distance = nearest_intersected_object(objects, origin, direction)
#        if nearest_object is None:
#            continue
#
#        # compute intersection point between ray and nearest object
#        intersection = origin + min_distance * direction
#
#        # image[i, j] = ...
#        print("%d/%d" % (i + 1, height))

#plt.imsave('image.png', image)
