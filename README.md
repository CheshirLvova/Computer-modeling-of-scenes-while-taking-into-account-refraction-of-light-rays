# Комп'ютерне моделювання сцен з урахуванням заломлення променів світла

Демонстрація сцен, що досліджувалися у курсовій роботі:

* [Сцена №1:]() показує різні квадратичних (математичних) форм трасування променів. Сімейство 3D-квадричних фігур включає найбільш знайомі математичні тривимірні фігури: сфери (еліпсоїди), циліндри, конуси, а також деякі форми, які не так добре відомі: параболоїди, гіперболоїди, гіперболічні параболоїди тощо. <br>

* [Сцена №2:]() Ця демонстрація дозволяє досліджувати нескінченну різноманітність квадратичних форм. Усі квадрики визначаються набором параметрів (зазвичай позначаються від A до J), які описують тип і вигляд фігури. Нещодавно я натрапила на маленьку перлину курсової роботи під назвою «Ray Tracing Arbitrary Objects on the GPU»  2004 року. У статті автори описують ефективний метод зберігання параметрів квадратичної форми (A-J) всередині акуратної матриці 4x4, яка добре вписується в пам'ять GPU. Будь-яку квадратичну форму можна легко побудувати, налаштувавши параметри A-J всередині матриці 4x4. Я реалізував їхню техніку для цієї демонстрації. Зробивши це ще далі, я надала у меню графічного інтерфейсу список стандартних заготовок форм (сфера, конус, параболоїд тощо), щоб ви могли побачити, як налаштовуються параметри більш відомих фігур. Я також перетворила ці параметри квадратної форми A-J у зручні повзунки графічного інтерфейсу, щоб ви могли легко погратися з параметрами та спостерігати, як тривимірні фігури, що простежуються.  <br>

* [Сцена №3: Поле Корнелла]() це більше тест, анжі демонстрація, спрямований на визначення точності візуалізації програмного забезпечення шляхом порівняння відображеної сцени з фактичною фотографією тієї ж сцени і став загальновживаною 3D-тестовою моделлю. 
