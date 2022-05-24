# Комп'ютерне моделювання сцен з урахуванням заломлення променів світла
Виконала:<br>
студентка групи ПМіМ-12 Львівського національного університету імені Івана Франка<br>
факультету Прикладної математики та інформатики (кафедри Інформаційних систем)<br>
Ковальчук Софія

Науковий керівник: <br>
асист. каф. ІС, канд. фіз.-мат. Наук<br>
Стельмащук Віталій<br>


## Демонстрація сцен, що досліджувалися у курсовій роботі:

* [Сцена №1: Дослідження форм та матеріалів](https://cheshirlvova.github.io/Computer-modeling-of-scenes-while-taking-into-account-refraction-of-light-rays/Quadric_Geometry_Showcase.html) показує різні квадратичних (математичних) форм трасування променів. Сімейство 3D-квадричних фігур включає найбільш знайомі математичні тривимірні фігури: сфери (еліпсоїди), циліндри, конуси, а також деякі форми, які не так добре відомі: параболоїди, гіперболоїди, гіперболічні параболоїди тощо. <br>

* [Сцена №2: Дослідження фігури](https://cheshirlvova.github.io/Computer-modeling-of-scenes-while-taking-into-account-refraction-of-light-rays/Quadric_Shapes_Explorer.html) Ця демонстрація дозволяє досліджувати нескінченну різноманітність квадратичних форм. Усі квадрики визначаються набором параметрів (зазвичай позначаються від A до J), які описують тип і вигляд фігури. Нещодавно я натрапила на маленьку перлину курсової роботи під назвою «Ray Tracing Arbitrary Objects on the GPU»  2004 року. У статті автори описують ефективний метод зберігання параметрів квадратичної форми (A-J) всередині акуратної матриці 4x4, яка добре вписується в пам'ять GPU. Будь-яку квадратичну форму можна легко побудувати, налаштувавши параметри A-J всередині матриці 4x4. Я реалізував їхню техніку для цієї демонстрації. Зробивши це ще далі, я надала у меню графічного інтерфейсу список стандартних заготовок форм (сфера, конус, параболоїд тощо), щоб ви могли побачити, як налаштовуються параметри більш відомих фігур. Я також перетворила ці параметри квадратної форми A-J у зручні повзунки графічного інтерфейсу, щоб ви могли легко погратися з параметрами та спостерігати, як тривимірні фігури, що простежуються.  <br>

* [Сцена №3: Поле Корнелла](https://cheshirlvova.github.io/Computer-modeling-of-scenes-while-taking-into-account-refraction-of-light-rays/Cornell_Box.html) це більше тест, аніж демонстрація, спрямований на визначення точності візуалізації програмного забезпечення шляхом порівняння відображеної сцени з фактичною фотографією тієї ж сцени і став загальновживаною 3D-тестовою моделлю.  <br>
![](https://upload.wikimedia.org/wikipedia/commons/2/24/Cornell_box.png)

## Список використаних джерел:
* [Посилання на ресурс з 3D-моделями, що були використані у прикладах](https://sketchfab.com/tags/opengl)
* [Посилання на ресурс з шейдерами, що були використані у прикладах (після додаткової обробки)](https://www.geeks3d.com/shader-library/)
* [Посилання на ресурс, що дозволяє демонстрацію перформансу результатів](http://github.com/mrdoob/stats.js)
1.	Тернер Уіттіс. «Покращена модель освітлення для затіненого дисплея», 1980 [Text].
2.	Роберт Кук, Томас Портер, Лорен Карпентер. «Розподілене трасування променів», 1984 [Text].
3.	J. Avro, and D. Kirk. A survey of ray tracing acceleration techniques. In An Introduction to Ray Tracing, A. Glassner, Ed., pages 201–262. Academic Press, San Diego, CA, 1989 [Text].
4.	Артур Аппель. «Деякі методики відтінку твердих тіл», 1969 [Text].
5.	Кевін Сафферн. «Ray Tracing from the Ground Up», 2007 [Text].
6.	HEKPIKS.ORG [Electronic resource](https://helpiks.org/3-2158.html) - Last access: 11.2021.
7.	NVidia Corporation, NVIDIA GPU Programming Guide Version 2.2.0, 2004 [Text].
8.	John Amanatides, Andrew Woo. A Fast Voxel Traversal Algorithm for Ray Tracing, 1987 [Text].
9.	[Michael McCool.](http://libsh.sourceforge.net/), 2004 [Electronic resource]
10.	Phong B.T. Illumination for computer generated pictures// Communications of ACM.  1975. – № 6. – Р. 311–317.
11.	Yunfan Zhang. FPGA Ray Tracer: [Electronic resource]. – [Режим доступy](http://www.eeweb.com/project/yunfan_zhang/fpga-ray-tracer)
12.	Юніс Мохаммад. Залучення блочної міжпіксельної інтерполяціх для прискорення алгоритму трасування променів / Мохаммад Юніс, Р.В. Мальчева, С.О. Ковалев // Машинобудування та техносфера ХХІ століття. / Сбірник ХVIII міжнародної наукової конференції. - Донецьк: ДонНТУ, 2011.
13.	- Т.4. - С.189-191 [Text].
14.	Лисиця В.Т. Колірні моделі та закони поширення світла / В. Т. Лисиця. – Х. : ХНУ імені В.Н. Каразіна, 2012. – 82 с
15.	Шикін Є. В. Комп’ютерна графіка. Полігональні моделі (рос.) / Є. В. Шикін, О. В. Борєсков. – М. : Діалог МІФІ,2001. – 462 с
16.	Han-Wei Shen. Ray tracing basics [Електронний ресурс]. – [Режим доступу](http://web.cse.ohiostate.edu/~hwshen/681/Site/Slidesfiles/basicalgo.pdf) (дата звернення: 19.10.2021). 
17.	Roth S.D. Ray casting for modeling solids // Computer Graphics and Image Processing. -1982. - № 18. - P. 109-144.
18.	Appel A. Some techniques for shading machine renderings of solids // AFIPS spring joint computer conference. IBM Research Center, Yorktown Heights, N.Y. - 1968. - P. 37-45.
19.	Foley J.D., van Dam A. Feiner S.K., Hughes J.F. Computer Graphics: Principles and Practice // Addison-Wesley Publishing Company. -   - P. 718-739.
20.	Phong B.T. Illumination for computer generated pictures// Communications of ACM. - 1975.   № 6.   P. 311-317.
21.	Foley J.D., van Dam A. Feiner S.K., Hughes J.F. Computer Graphics: Principles and Practice // Addison-Wesley Publishing Company. – 1996. – Р. 718–739.
