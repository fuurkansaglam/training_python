RAM’in Heap ve Stack adlı alanları sayesinde veriler depolanabilir.
1-Stack Nedir, nasıl çalışır?
int, double, short gibi değer tipleri Stack içerisinde yer kaplar. 
Statik bir yapıdır. Daha hızlı çalışır.
Bu yüzden 
x = 2  Stack kısmında yer kaplar.
(çünkü int bir değişken)

2-Heap Nedir, nasıl çalışır?
Class, string gibi yapılar Heap içerisinde yer alır. 
Dinamik bir yapıdır (genişletilebilir).
Bu yüzden 
arabalar = ['ford', 'dodge']  Heap kısmında yer kaplar.
‘ford’, ‘dodge’ string değerleri heap kısmında depolanır. ‘arabalar’ degiskeni ise stack kısmında depolanır.
Bu yönetimi RAM kendisi yapar. Ancak kod yazarken bu ayrımın bilinmesi RAM yönetimi için önemlidir.

Örneğin:
    OUTPUT:  
Olacaktır. X’in Stack (statik) yer kaplamasından dolayı y değerine sonradan tanımlanan x değeri olan 3 atanmamış olacaktır.

      OUTPUT:  
Şeklinde olacaktır. Çünkü bu listedeki veriler Heap kısmında depolanmış ve dinamik bir yapıya sahiptir.

Garbage Collector Nedir?
Garbage Collector yazılan programın alanı daha verimli ve efektif kullanmasını sağlayan bir mekanizmadır. Bazı dillerde manuel çalıştırılırken Python dilinde otomatik olarak çalışmaktadır. GC, kullanılmayan nesneleri ve gereksiz bellek alanlarını otomatik olarak temizler.
GC Ne işe yarar?
Daha verimli bir bellek yönetimi sağlar. Bellek doluluğu sebepli performans kaybını engeller.
GC Nasıl çalışır?
Öncelikle nesneleri takip eder ve işaretler. G0,G1,G2 olarak işaretleyebilir.
G0: Genç nesneler – yeni oluşturulan nesneler
G1: Orta nesneler – daha uzun süreli kullanılan nesneler
G2: Yaşlı nesneler – uzun süredir var olan nesneler
Nesneler ilk olarak G0 olarak konaklar. Ağırlıklı olarak G0 nesneler daha sık temizlenir, temizlik yapılırken daha uzun süreli var olacak olan nesneler G1, G2 işaretlerini alır ve temizlenmez.
