# Fashion_analysis
Proje amacı : Kullanıcı tarafından kıyafet resimleri yüklenir.İlk önce Detectron2 ile eğitilen modelden ana kategoriler bounding box,sınıf ve segmentasyon sonuçları alınır.Daha sonra tahminde çıkan ana sınıflara göre sınıflandırma modellerinde bir tahmin döndürülür.En son tahmin edilen sınıfların baskın rengi tahmin edilir.

##Modeller ve sınıfları:

1.Detectron2 Modeli(İlk ana model,Segmentasyon,Object detection ve sınıflandırma yapan model)

	1.1 Upperbody(Üst gövdeye ait sınıfı bulan sınıflandırma modeli)
	
		1.1.1 Cardigan
		
		1.1.2 Jacket
		
		1.1.3 Shirt_blouse(Gömlekteki kol uzunluğunu bulan sınıflandırma modeli)
		
			1.1.3.1 Short_length(kol uzunluğu)
			
			1.1.3.2 Wrist_length(kol uzunluğu)
			
		1.1.4 Sweater(Kazaktaki yaka tipini bulan sınıflandırma modeli)
		
			1.1.4.1 Round(neck)(Yaka tipi)
			
			1.1.4.2 Turtle(neck)(Yaka tipi)
			
			1.1.4.3 v-neck(Yaka tipi)
			
		1.1.5 Top_t_shirt_sweatshirt
		
		1.1.6 vest
		
	1.2 Lowerbody(Alt gövdeye ait sınıfı bulan sınıflandırma modeli)
	
		1.2.1 Pants(Pantalona ait sınıfı bulan sınıflandırma modeli)
		
			1.2.1.1 Capri
			
			1.2.1.2 Sailor 
			
			1.2.1.3 Sweat
			
		1.2.2 Shorts
		
		1.2.3 Skirt
		
			1.2.3.1 Skirt Length(Eteğin boyunu bulan sınıflandırma modeli)
			
				1.2.3.1.1 Maxi
				
				1.2.3.1.2 Midi
				
				1.2.3.1.3 Mini
				
			1.2.3.1 Skirt Opening(Eteğin açılış şeklini bulan sınıflandırma modeli)
			
				1.2.3.1.1 Fly Opening
				
				1.2.3.1.2 No Opening
				
	1.3 Wholebody
	
	1.4 Accessories(Aksesuara ait sınıfı bulan sınıflandırma modeli)
	
		1.4.1 Bag,wallet
		
		1.4.2 Glasses
		
		1.4.3 Hat
		
		1.4.4 Tie
		
		1.4.5 Umbrella
		
		1.4.6 Watch
		
	1.5 Footwear
