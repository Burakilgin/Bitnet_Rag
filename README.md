Llama 3.1 8b modeli ile geliştirilmiş RAG sistem modelidir. Bu modelde düzenleme yapılarak Microsoft/Bitnet b1.58-2B-4T modeli entegre edilmiştir. Hız ve geliştirme amaçlı olarak CPU verimlilik testi amacıyla bu model tercih edilmiştir. Modelde uyarı mesajları görünebilir, ilerleyen versionlarda güncellemeler gelecek. 

--------

Repo'yu klonlayıp daha sonra main dosyasını çalıştırmanızdan sonra Bitnet modelini kodun içerisindeki transformers kütüphanesi tarafından indirilmeye başlanacaktır. 

!!!! UYARI !!!!
--- Lütfen modeli çalıştırmadan önce RAG yapmak istediğiniz dosyanın dosya yolunu "knowledge_base.py" dosyası üzerinden değiştiriniz. Daha sonra "main.py" dosyasını çalıştırmanızdan sonra gerekli olan tüm adımlar çalışıp model terminal üzerinden çıktı üreterek iletişime geçecektir. Model bir kere çalışmaktadır. Test bazlı çalışma yapılmasından dolayı şu anda her soru cevap sonrası yeniden "main.py" dosyasının çalıştırılması gerekmektedir. Transformers kütüphanesi tekrar tekrar indirme yapmadan var olan modeli sistemde tanıyarak kullanım sağlamaktadır. 

--------

Geliştirme için her türlü öneri ve yardıma açığım. Mail yoluyla veya Community kısmında iletişime geçebilirsiniz.

İyi Çalışmalar
