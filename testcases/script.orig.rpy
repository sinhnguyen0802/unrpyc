
image bg lecturehall = "lecturehall.jpg"
image bg uni = "uni.jpg"
image bg meadow = "meadow.jpg"
image bg club = "club.jpg"

image sylvie normal = "sylvie_normal.png"
image sylvie giggle = "sylvie_giggle.png"
image sylvie smile = "sylvie_smile.png"
image sylvie surprised = "sylvie_surprised.png"

image sylvie2 normal = "sylvie2_normal.png"
image sylvie2 giggle = "sylvie2_giggle.png"
image sylvie2 smile = "sylvie2_smile.png"
image sylvie2 surprised = "sylvie2_surprised.png"


define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")


label start:
    $ bl_game = False

    play music "illurock.ogg"

    Hội trường
 
    "Bài giảng nghe cuốn vl ."
    "nhưng thật ra tôi éo quan tâm lắm."
    "Bởi vô số những chuyện khác đang làm tôi bận tâm hơn nhiều."
    "Và tất cả mọi suy nghĩ của tôi kết thúc với một dấu hỏi to tướng trong đầu ."
    "Một dấu chấm hỏi mà tôi cần ai đó giải đáp+."

    scene bg uni
    with fade

    "Khi tôi bước ra khỏi trường đại học, tôi đã nhìn thấy cô ấy."

    Nghỉ học

    "Cô ấy từng là một người vô cùng tuyệt vời."
    "Tôi quen biết cô ấy kể từ khi còn là loli."
    "Và well, tất nhiên cô ấy luôn luôn là một người bạn tốt"
    "Nhưng..."
    "gần đây..."
    "tôi nghĩ..."
    "... tôi muốn quất cô ấy."
    "Đuỵt mọe, tất nhiên tôi đéo muốn làm friend zone."
    "cuối cùng tôi đã quyết định..."

    menu:
        "... nói với cô ấy ngay lập tức.":
            em ey
        "... đéo nói.":
            cút 

label rightaway:

    sylvie nở cụ cười trắng tinh như hoa cúc

    s "2 đứa mình về chung được hong?"
    m "ok bro..."
    "Giọng tôi run vãi cả bíp ạ."

    cánh đồng cỏ dần dần xuất hiện

    "thúng tôi đi đến những bụi chuối bên ngoài thị trấn."
    "mùa thu thật đẹp."
    "khi cô ấy còn là loli, chúng tôi thường vui đùa tại nơi này, ôi bao nhiêu kĩ niệm lại ùa về trong tôi."
    m "Hey... ummm..."

    sylvie nở một nụ cười đầy triều mến
    

    "cô ấy quay sang tôi nở nụ cười nằm dọc."
    "tôi sẽ hỏi cô ấy..."
    m "Ummm... anh sẽ..."
    m "em sẽ làm nhân vật chính cho cuốn tiểu thuyết của anh chứ?"

    vẻ mặt ngạc nhiên

    "Im lặng."
    "cô ấy bị sốc. và rồi..."

    show sylvie smile

    s "chắn chắn rồi nhưng tiểu thuyết là gì? \"visual novel?\""

    menu:
        "đó là một câu chuyện với hình ảnh.":
            jump vn
        "hentai.":
            jump hentai

label vn:

    m "Nó là chuyện với nhạc và hình."
    m "và lựa chọn của mày sẽ ảnh hưởng đến cốt truyện đó thằng lon."
    s "vậy nó giống những cuốn sách phiêu lưu?"
    m "á đù, đúng vcl,anh muốn làm một câu chuyện lãng mạn."
    m "Và anh nghĩ em có thể hepl me...tôi biết bạn thích vẽ mà."

    show sylvie normal

    s "ok thôi bro, tôi nghĩ toi k làm bạn thất vọng đâu, cùng lắm là tuyệt vọng thôi."
    m "không đâu bro, tôi tin bạn."

    jump marry

label hentai:

    $ bl_game = True

    m "Game s e x?."
    s "Giống như phim?"
    s "em đã luôn muốn thử điều này."
    s "được rồi, đuỵt thoi nào!"

    hide sylvie
    with dissolve

    "..."

    m "không không, nó đéo phải thứ mình nghỉ!"

    jump marry

label marry:

    scene black
    with dissolve

    "--- years later ---"

    scene bg club
    with dissolve

    "và vì vậy , chúng tôi đã trở thành những nhà tạo lập game hen."
    "chúng tôi sáng tạo vô số kiểu lạ."

    if bl_game:
        "Nhưng ngoại trừ trò boy love mà cô ấy muốn làm."

    "cho đến một ngày..."

    show sylvie2 normal
    with dissolve

    s "Hey..."
    m "hể?"

    show sylvie2 giggle

    s "đám cưới với em không!"
    m "cái đéo gì vậy???"

    show sylvie2 surprised

    s "vậy, anh không muốn đều đó sao?"
    m "không không, đime muốn chứ."

    show sylvie2 smile

    s "nhìn?chúng ta đã làm rất nhiều chuyện bên nhau, đuỵt, đuỵt và đuỵt...."
    s "... và khi tình yêu anh đến với em, thì em cũng vậy."
    m "Hmmm, hay rất hay bro."

    show sylvie2 giggle

    s "não tôi giờ chỉ suy nghxi được nhiêu đó."
    m "nhưng nó tuyệt."

    show sylvie2 normal

    s "em biết, vậy chúng ta kết hôn được không?"
    m "tất nhiên rồi, anh cũng định hỏi em về điều đó..."
    s "em biết, nhưng anh là thằng óc lồn, nên em phải nói điều này. "
    m "tôi đoán...nó chỉ là một câu hỏi... chỉ cần hỏi vào đúng thời điểm."

    show sylvie2 giggle

    s "nhưng giờ, hôn em đi làm ơn!"

    scene black
    with dissolve

    "và chúng tôi kết hôn."
    "và thế là chúng tôi địt nhau."
    "cùng nhau hạnh phúc mãi mãi về sau."

    ".:. Good Ending."

    return

label later:

    scene black
    with dissolve

    "And so I decided to ask her later."
    "But I was indecisive."
    "I couldn't ask her that day, and I couldn't ask her later."
    "I guess I will never know now."

    ".:. Bad Ending."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
