# Computer-modeling-of-scenes-while-taking-into-account-refraction-of-light-rays

<h3>Classic Scenes / Ray Tracing History</h3>

<img src="https://github.com/erichlof/THREE.js-PathTracing-Renderer/blob/gh-pages/readme-Images/4-Figure7-1.png" width=30% height=30%>

Arthur Appel is credited with the first formal mention of Ray Tracing (raycasting and shadow rays, shown above) in his 1968 paper [Some Techniques for Shading Machine Renderings of Solids](https://docs.google.com/viewer?url=https%3A%2F%2Fohiostate.pressbooks.pub%2Fapp%2Fuploads%2Fsites%2F45%2F2017%2F09%2Fshading-appel.pdf) while working at IBM Research (TJW Center).  Mr. Appel used this new technique to help visualize machine parts and architectural concepts on printed paper in black and white.  The scene data was sent to an IBM 1627 (Calcomp) digital plotter that cleverly used text characters (like '+') with different spacing and brightness to differentiate the various shading of sides of a 3D model under a virtual light source.  Here are a few examples of Mr. Appel's digital plot renderings from his 1968 paper:

<img src="https://github.com/erichlof/THREE.js-PathTracing-Renderer/blob/gh-pages/readme-Images/2-Figure2-1.png" width=20% height=20%> <img src="https://github.com/erichlof/THREE.js-PathTracing-Renderer/blob/gh-pages/readme-Images/4-Figure3-1.png" width=70% height=70%>

For reference, here is a link to all the images featured in the research paper: [Original Appel Renderings](https://www.semanticscholar.org/paper/Some-techniques-for-shading-machine-renderings-of-Appel/14a97553cf2d5414ec94b14bf22700b1b3c93a0d#extracted) (click on the 'View All 14 Figures and Tables' button below the first images).

And here is a demo that lets you literally 'jump into' Appel's 1968 research paper and experience his groundbreaking techniques of per-pixel raycasting and shadow rays:
* [Shading Machine Renderings of Solids demo](https://erichlof.github.io/THREE.js-PathTracing-Renderer/Classic_Scene_Appel_ShadingMachineRenderingsOfSolids.html) <br>

Scenes that used to take several minutes on Appel's digital plotting device now run at 60 fps in your browser!  I think Arthur would get a kick out of dragging the sunlight around in real time on his classic scenes!

Until now (2021), actual photos of Arthur Appel were not publicly available (none can be found with a thorough internet search).  All that was known was that he was working at IBM Research (TJW Center) at the time he wrote this seminal 1968 paper.  I really wanted to see what Mr. Appel looked like, and to share and celebrate his image and contributions to the field of Ray Tracing and Rendering.  With a little hesitation at first, I reached out to the IBM Corporate Archives in New York to see if they might have any remaining employee portraits of Arthur Appel.  I'm so glad I did, because I met (via email) a wonderful IBM Archive employee, Max Campbell, who kindly searched the entire archives and found 2 rarely-seen photos of Mr. Appel.  Since these images are copyrighted by IBM (and NOT a part of my repo's CC License), Max also kindly and graciously helped me to obtain permission from IBM to share these historic photos of the man who started it all!  Click on the images to see the full resolution photos:

<img src="https://github.com/erichlof/THREE.js-PathTracing-Renderer/blob/gh-pages/readme-Images/1982_December_Arthur%20Appel_IBM%20Research%20Magazine.png" width=20% height=20%> <br>
Arthur Appel, from the IBM Research Employee Gallery, ca. 1982
Reprint Courtesy of IBM Corporation © <br>

<img src="https://github.com/erichlof/THREE.js-PathTracing-Renderer/blob/gh-pages/readme-Images/1983_December_Arthur%20Appel_IBM%20Research%20Magazine.png" width=20% height=20%> <br>
Arthur Appel demonstrating display architecture, from IBM Research Magazine ca. 1983
Reprint Courtesy of IBM Corporation © <br>

Many thanks to Max Campbell at IBM Research Archives for locating these rare photos and helping me to obtain permission to share them with everyone who is interested in ray tracing!  It is so nice to be able to finally put a face with the name of one of my ray tracing heroes.  Thank you Arthur Appel for your historic contributions to the field of Computer Graphics! <br>
<br>


![](readme-Images/Whitted_1979.jpg)

While working at Bell Labs and writing his now-famous paper [An Improved Illumination Model for Shaded Display](http://artis.imag.fr/Members/David.Roger/whitted.pdf), J. Turner Whitted created an iconic ray traced scene which showcased his novel methods for producing more realistic images with a computer. Beginning work in 1978, he rendered a handful of scenes featuring spheres and planes with various materials and reflectivity, so that these images would be included in his paper (which would be published in June 1980).  Then for an upcoming SIGGRAPH conference submission, Whitted decided to create an animated sequence of individual rendered images.  Thus the first ever ray traced animation was born!  This style of putting together single frames of pre-rendered images would continue through a great lineage of movies such as Tron, Toy Story, Cars, all the way to current animated feature films.     

[Vintage 1979 Video: 'The Compleat Angler' by J. Turner Whitted](https://youtu.be/0KrCh5qD9Ho)

Although this movie appears as a smooth animation, it took around 45 minutes to render each individual frame back in 1979!  Fast forward to today and using WebGL 2.0 and the parallel processing power of GPUs, here is the same iconic scene rendered at 60 times a second in your browser! : <br>
* [The Compleat Angler demo](https://erichlof.github.io/THREE.js-PathTracing-Renderer/Classic_Scene_Whitted_TheCompleatAngler.html) <br>

Thank you Dr. Whitted for your pioneering computer graphics work and for helping to start the rendered animation industry!  <br> 
<br>

In 1986 James T. Kajiya published his famous paper [The Rendering Equation](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.63.1402), in which he presented an elegant and profound unifying integral equation for rendering.  Since the equation is infinitely recursive and hopelessly multidimensional, he suggests using Monte Carlo integration (sampling and averaging) in order to converge on a solution.  Thus Monte Carlo path tracing was born, which this repo follows very closely.  At the end of his paper he included a sample rendered image that demonstrates global illumination through Monte Carlo path tracing:

![](readme-Images/kajiya.jpg)

And here is the same scene from 1986, rendered in real-time: <br>
* [The Rendering Equation Demo](https://erichlof.github.io/THREE.js-PathTracing-Renderer/Classic_Scene_Kajiya_TheRenderingEquation.html) <br>
<br>

<h4>Bi-Directional Path Tracing</h4>
In December of 1997, Eric Veach wrote a seminal PhD thesis paper on methods for light transport http://graphics.stanford.edu/papers/veach_thesis/  In Chapter 10, entitled Bi-Directional Path Tracing, Veach outlines a novel way to deal with difficult path tracing scenarios with hidden light sources (i.e. cove lighting, recessed lighting, spotlights, etc.).  Instead of just shooting rays from the camera like we normally do, we also shoot rays from the light sources, and then later join the camera paths to the light paths.  Although his full method is difficult to implement on GPUs because of memory storage requirements, I took the basic idea and applied it to real-time path tracing of his classic test scene with hidden light sources.  For reference, here is a rendering made by Veach for his 1997 paper:

![](readme-Images/Veach-BiDirectional.jpg)

And here is the same room rendered in real-time by the three.js path tracer: <br>
* [Bi-Directional PathTracing Demo](https://erichlof.github.io/THREE.js-PathTracing-Renderer/Bi-Directional_PathTracing.html) <br>

The following classic scene rendering comes from later in the same paper by Veach.  This scene is intentionally difficult to converge because there is no direct light, only indirect light hitting the walls and ceiling from a crack in the doorway.  Further complicating things is the fact that caustics must be captured by the glass teapot on the coffee table, without being able to directly connect with the light source.

![](readme-Images/Veach-DifficultLighting.jpg)

And here is that scene rendered in real-time by the three.js path tracer: Try moving the GUI slider to open and close the door! <br>
* [Difficult Lighting Classic Test Scene Demo](https://erichlof.github.io/THREE.js-PathTracing-Renderer/Bi-Directional_Difficult_Lighting.html) <br>

I only had the above images to go on - there are no scene dimensions specifications that I am aware of.  However, I feel that I have captured the essence and purpose of his test scene rooms.  I think Veach would be interested to know that his scenes, which probably took several minutes if not hours to render back in the 1990's, are now rendering real-time in a web browser! :-D

For more intuition and a direct comparison between regular path tracing and bi-directional path tracing, here is the old Cornell Box scene again but this time there is a blocker panel that blocks almost all of the light source in the ceiling.  The naive approach is just to path trace normally and hope that the camera rays will be lucky enough to find the light source:
* [Naive Approach to Blocked Light Source](https://erichlof.github.io/THREE.js-PathTracing-Renderer/Compare_Uni-Directional_Approach.html) As we can painfully see, we will have to wait a long time to get a decent image!
Enter Bi-Directional path tracing to the rescue!:
* [Bi-Directional Approach to Blocked Light Source](https://erichlof.github.io/THREE.js-PathTracing-Renderer/Compare_Bi-Directional_Approach.html) Like magic, the difficult scene comes into focus - in real-time! <br> <br> <br>




<h2>FEATURES</h2>

* Real-time interactive Path Tracing at 30-60 FPS in your browser - even on your smartphone! ( What?! )
* First-Person camera navigation through the 3D scene.
* When camera is still, switches to progressive rendering mode and converges on a highest quality photo-realistic result!
* The accumulated render image will converge at around 500-3,000 samples (lower for simple scenes, higher for complex scenes).
* My custom randomized Direct Light targeting now makes images render/converge almost instantly!
* Both Uni-Directional (normal) and Bi-Directional path tracing approaches available for different lighting situations.
* Support for: Spheres, Planes, Discs, Quads, Triangles, and quadrics such as Cylinders, Cones, Ellipsoids, Paraboloids, Hyperboloids, Capsules, and Rings/Torii. Parametric/procedural surfaces (i.e. terrain, clouds, waves, etc.) are handled through Raymarching.
* Constructive Solid Geometry(CSG) allows you to combine 2 shapes using operations like addition, subtraction, and overlap.
* Support for loading models in .gltf and .glb formats
* BVH (Bounding Volume Hierarchy) greatly speeds up rendering of triangle models in gltf/glb format (tested up to 800,000 triangles!)
* Current material options: Metallic (mirrors, gold, etc.), Transparent (glass, water, etc.), Diffuse(matte, chalk, etc), ClearCoat(cars, plastic, polished wood, billiard balls, etc.), Translucent (skin, leaves, cloth, etc.), Subsurface w/ shiny coat (jelly beans, cherries, teeth, polished Jade, etc.)
* Solid transparent objects (i.e. glass tables, glass sculptures, tanks filled with water or other fluid, etc) now obey the Beer-Lambert law for ray color/energy attenuation.
* Support for PBR materials on models in gltf format (albedo diffuse, emissive, metallicRoughness, and normal maps)        
* Diffuse/Matte objects use Monte Carlo integration (a random process, hence the visual noise) to sample the unit-hemisphere oriented around the normal of the ray-object hitpoint and collects any light that is being received.  This is the key-difference between path tracing and simple old-fashioned ray tracing.  This is what produces realistic global illumination effects such as color bleeding/sharing between diffuse objects and refractive caustics from specular/glass/water objects.
* Camera has Depth of Field with real-time adjustable Focal Distance and Aperture Size settings for a still-photography or cinematic look.
* SuperSampling gives beautiful, clean Anti-Aliasing (no jagged edges!)
