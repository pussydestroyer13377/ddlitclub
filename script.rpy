define mc = ("Lâm Huy Hoàng")
define banthan = "Bản thân"
define tien1 = "Tiến Võ"
define tien2 = "TrọTiên"

image hanhlang1 = im.Scale("hanhlang.jpg", 1920, 1080)
image lib1 = im.Scale("lib.jpg", 1920, 1080)
image bedroom1 = im.Scale("bedroom.jpg", 1920 , 1080)
image d2_1 = im.Scale("d2.jpg", 1920 , 1080)
image nightstreet1 = im.Scale("night_street.jpg", 1920 ,1080)
image benhvien = im.Scale("bv.jpg", 1920, 1080)
image nhatiennight = im.Scale("nhatiennight.jpg", 1920, 1080)
image nhatien = im.Scale("nhatien.png", 1920 , 1080)
image bacho = im.Scale("bacho.jpg", 1920, 1080)
image phongvantien = im.Scale("phongtien.jpg", 1920, 1080)
image tien_hang1 = "tienhang.jpg"

label start:
play music "ho.mp3"
### KIỂM TRA VÀ NHẬP TÊN
"Tôi đã luôn nghĩ về việc chọn một tên cho mình"
$ player_name = renpy.input("Tên của bạn là gi?")
$ player_name = player_name.strip()
if player_name == "":  ## CHECK SIÊU TO KHỔNG LỒ
    $ player_name ="Võ Văn Trung"
if player_name == "Chó Toàn":
    $ player_name ="Võ Văn Trung"
if player_name == "Đỗ Minh Toàn":
    $ player_name ="Võ Văn Trung"
if player_name == "Trần Thị Thanh Xuân":     # KO CÓ AND VÀ TABLE TRONG RPYC =((
    $ player_name ="Võ Văn Trung"
if player_name == "Tran thi thanh xuan":
    $ player_name ="Võ Văn Trung"
if player_name == "Do van chung":
    $ player_name ="Võ Văn Trung"
if player_name == "Đỗ Văn Chung":
    $ player_name ="Võ Văn Trung"
if player_name == "Toàn":
    $ player_name ="Võ Văn Trung"
if player_name == "ToanDo":
    $ player_name ="Võ Văn Trung"
if player_name == "Toàn Chó":
    $ player_name ="Võ Văn Trung"
if player_name == "Toan":
    $ player_name ="Võ Văn Trung"
if player_name == "Do Minh Toan":
    $ player_name ="Võ Văn Trung"
if player_name == "Minh Toàn":
    $ player_name ="Võ Văn Trung"
if player_name == "Toàn Láo":
    $ player_name ="Võ Văn Trung"
if player_name == "minh toan":
    $ player_name ="Võ Văn Trung"
if player_name == "do minh toan":
    $ player_name ="Võ Văn Trung"
if player_name == "cho toan":
    $ player_name ="Võ Văn Trung"
if player_name == "tran thi thanh xuan":
    $ player_name ="Võ Văn Trung"
if player_name == "thanh xuan":
    $ player_name ="Võ Văn Trung"
if player_name == "thanhxuan":
    $ player_name ="Võ Văn Trung"
if player_name == "do van chung":
    $ player_name ="Võ Văn Trung"
if player_name == "van chung":
    $ player_name ="Võ Văn Trung"
if player_name == "vanchung":
    $ player_name ="Võ Văn Trung"
if player_name == "toan":
    $ player_name ="Võ Văn Trung"
if player_name == "toan do":
    $ player_name ="Võ Văn Trung"
if player_name == "do toan":
    $ player_name ="Võ Văn Trung"
if player_name == "Toàn Đỗ":
    $ player_name ="Võ Văn Trung"
if player_name == "ToanDo":
    $ player_name ="Võ Văn Trung"
if player_name == "Toan Do":
    $ player_name ="Võ Văn Trung"
if player_name == "100 uvk":
    $ player_name ="Võ Văn Trung"
if player_name == "do toan":
    $ player_name ="Võ Văn Trung"
if player_name == "chung xuân":
    $ player_name ="Võ Văn Trung"
if player_name == "Chung Xuân":
    $ player_name ="Võ Văn Trung"
if player_name == "chung xuan":
    $ player_name ="Võ Văn Trung"
# alex mahan 2.0
scene d2_1
"Một ngày nọ..."
"Mình tên là %(player_name)s"
"Là một học sinh lớp 9"
"Trường THCS Đống Đa"
"Cũng như bao mọi người, năm nay là năm cuối của mình ở ngôi trường này"
"Và mình cũng có một người bạn đã quen từ lớp 6 tới giờ"
"Ngày nào cũng đi đến trường cùng với mình"
show tien3:
    xalign 0.25
    yalign 0.5
tien1 "Chào!"
tien1 "Mình đi chung với nhau nhé"
hide tien3
"Mình cũng không nỡ lòng nào từ chối được"
"Và bạn ấy cũng là trưởng câu lạc bộ ngữ văn của trường"
show tien3:
    xalign 0.25
    yalign 0.5
tien1 "Nè nè"
tien1 "Muốn vào chung câu lạc bộ với mình không?"
hide tien3
"Thôi cảm ơn"
"À"
"sắp đánh trống rồi lo tới trường nhanh đi"
tien1 "Ok"
hide d2_1
scene truong
show hoang:
  xalign 0.75
  yalign 0.5
mc "Em có phải là %(player_name)s không?"
mc "Bạn tiến đã yêu cầu thầy cho em vào câu lạc bộ ngữ văn của trường"
mc "Em chắc chắn muốn vào không?"
menu:
 banthan "Có nên vào không?"
 "Có":
   jump gianhap

 "Không":
   jump kogianhap
label gianhap:
 "Ok, em nhớ 8g sáng ngày mai xuống phòng thư viện."
 hide hoang
 jump xuongthuviendau
label kogianhap:
 mc "Tại sao em lại không gia tham gia?"
 mc "Thầy đã tạo điều kiện cho em vậy mà."
 mc "Bạn em vì vậy cũng buồn lắm đó"
 banthan "..."
 hide hoang
 jump xuongthuvien_kogianhap
label xuongthuviendau:  # thư viện chính set1
 "..."
 hide truong
 scene lib1
 show tien3:
  xalign 0.75
  yalign 0.5
 "Tiến" "Chào bạn!"
 "Tiến" "Mình tên Võ Văn Tiến"
 "Tiến" "Rất vui được gặp bạn"
 "Tiến" "Chắc cũng biết mình rồi nha"
 "Tiến" "Mình là trưởng câu lạc bộ này"
 "Tiến" "Nhớ hòa thuận với nhau nhé"
 hide tien3
 show hatien:
  xalign 0.75
  yalign 0.5
 tien2  "Lô cc"
 tien2  "Làm không đàng hoàng tao đuổi mày ra khỏi câu lạc bộ đó."
 hide hatien
 show tien3:
     xalign 0.25
     yalign 0.5
 tien1 "Xin lỗi bạn, Trong Tiến hơi bị nóng tính"
 menu:
     banthan "Có nên ra khỏi không?"
     "Nên":
      jump banluan_thuyetphuc
     "Không nên":
       jump banluanfin1
label xuongthuvien_kogianhap: #kogianhap xíu return qua xuongthuviendau
 hide truong
 scene black
 with fade
 "Sau khi lên lớp..."
 "Ai có tên trong danh sách sau xuống phòng thư viện nha"
 "%(player_name)s sẽ xuống dưới thư viện trường!"
 "..."
 banthan "%(player_name)s ?"
 jump xuongthuviendau
label banluan1:
    "Ok vậy tụi mình bắt đầu nha"
    jump banluanfin
label banluan_thuyetphuc: # to banluan
   hide hatien
   tien1 "Mới buổi gặp đầu tiên mà đã vậy rồi"
   banthan "Nhưng thằng này nó khó tính vãi"
   banthan "Làm gì cũng chửi hết"
   tien1 "Tình nghĩa anh em chúng ta có chắc bền lâu"
   tien1 "Thôi bạn tham gia với chúng mình luôn nha"
   banthan "Ok, được thôi"
   jump banluanfin
label banluanfin:
    "Vậy tụi mình sẽ bắt đầu với những hoạt động đầu tiên."
    jump banluan_Taphop
label banluanfin1: # fix cho menu
    "Vậy tụi mình sẽ bắt đầu với những hoạt động đầu tiên."
    jump banluan_Taphop
label banluan_Taphop:
hide hatien
show tien3:
    xalign 0.75
    yalign 0.5
tien1 "Ok.."
tien1 "Những hoạt động đầu tiên của clb là"
tien1 "Ermm..."
hide tien3
show hatien:
    xalign 0.5
    yalign 0.5
tien2 "NHANH LÊN COI"
hide hatien
show tien3:
    xalign 0.75
    yalign 0.5
tien1 "Viết thơ và làm văn"
hide tien3
"Mình có khiếu về mấy cái này đâu mà mời mình vào làm gì vậy?"
banthan "Ừmmm mọi người"
"hả?"
banthan "Mình có giỏi mấy cái này đâu?"
show tien3:
    xalign 0.75
    yalign 0.5
tien1 "Thôi mà"
tien1 "Tụi mình sẽ giúp bạn giỏi lên được mà"
banthan "umm ok"
tien1 "Được rồi mọi người, bây giờ mình sẽ vào chủ đề chính luôn nha"
tien1 "Và đó là về.."
tien1 "Thơ!"
menu:
    banthan "Thơ nên viết về cái gì đây?"
    "Cái khác":
        $ yeucauthemhoatdong = True             # FLAG 1 : yeucauthemhoatdong_OBSOLETE
        banthan "Mình sẽ làm về .."
        jump banluan_Taphop2
    "Tình bạn":
       $ koyeucauthemhoatdong = True            # FLAG 2 : koyeucauthemhoatdong_OBSOLETE
       banthan  "Mình sẽ làm về tình bạn!"
       tien1  "Nghe được đó"
       jump banluan_Taphop2_alt
label banluan_Taphop2:
    hide lib1
    scene white
    tien1 "Vậy %(player_name)s muốn thêm thứ gì nữa"
    banthan "..."
    banthan "Mình muốn thêm ..."
    $ hoatdongmoi = renpy.input("Bạn muốn thêm hoạt động gì?")  # FLAG 3 : hoatdongmoi
    $ hoatdongmoi = hoatdongmoi.strip() # khử và thêm flag
    tien1 "Được rồi vậy %(player_name)s sẽ về nhà làm về thơ"
    banthan "Thơ gì?"
    tien1 "Thơ gì cũng được"
    show hatien:
        xalign 0.5
        yalign 0.5
    tien1 "Được rồi!"
    tien1 "Vậy tối nay các bạn về làm cho mỗi người một bài thơ của riêng mình nhé!"
    hide tien1
    tien2 "Ok"
    hide tien2
    show d2 #đường
    "pause"
    jump chuong2
label banluan_Taphop2_alt:
    hide lib1
    scene white
    tien1 "Vậy tối nay các bạn sẽ về làm bài thơ của riêng mình nhé!"
    show hatien
    "OK!"
    hide tien1
    hide hatien
    hide white
    scene d2
    "pause"
    jump chuong2
label chuong2:
    stop music
    hide lib1
    play music "lol.mp3"
    scene black
    "Chương 2: Sự khởi đầu"
    hide black
    scene bedroom1
    with fade
    "Haizzzz"
    banthan "Vậy là một ngày nữa sắp kết thúc rồi"
    banthan "Mình nên viết về gì ta?"
    "..."
    banthan "À nhớ rồi!"
    $ tho1 = renpy.input("Hãy viết thơ của bạn:")
    $ tho1 = tho1.strip()
    banthan "Vậy chắc được rồi!"
    banthan "Ồ 11h30 rồi!"
    banthan "Thôi đi ngủ"
    hide bedroom1
    #### sáng
    scene black
    play sound "alarm.mp3"
    hide black
    scene white
    with fade
    banthan "Trời ơi mới đây đã 6 giờ rồi"
    banthan "Thôi tới trường nhanh không thôi trễ giờ mất"
    hide white
    with dissolve
    scene d2
    banthan "Trời ơi xe đông quá!!"
    hide d2
    scene truong
    with fade
    "Tới cổng rồi!"
    hide truong
    with fade
    scene hanhlang1
    "*Chạy hì hụt"
    hide hanhlang1
    with fade
    scene white
    with fade
    "*Bước vào thư viện*"
    "Mở cửa"
    banthan "Chào mọi người!"
    hide white
    with dissolve
    scene lib
    show tien3:
        xalign 0.75
        yalign 0.5
    show hatien:
        xalign 0.5
        yalign 0.5
    ".."
    "Chào.."
    "À hôm qua quên nói với %(player_name)s rằng hôm nay ..."
    hide tien_shy
    hide tien3
    hide hatien
    "Đột nhiên có tiếng mở cửa mạnh.."
    "*Hì hụt*"
    "Chào mọi người!"
    hide tien3
    show bntblursed:
        xalign 0.5
        yalign 0.5
    with fade
    "Bảo Ngọc Trần" "MÌNH"
    "Bảo Ngọc Trần" "tới trễ xin lỗi mọi người!"
    show tien_shy:
        xalign 0.75
        yalign 0.5
    with fade
    hide bntblursed
    tien1 "Không sao đâu bạn"
    tien1 "Đây là Bảo Ngọc Trần nha! bạn %(player_name)s"
    banthan "Ừm ok"
    hide bntblursed
    with fade
    tien1 "Errmm"
    tien1 "Như ngày hôm qua mình có dặn các bạn làm thơ đúng không?"
    show hatien:
        xalign 0.25
        yalign 0.5
    tien2 "Có"
    hide hatien
    with fade
    banthan "Có"
    tien1 "Ok, vậy các bạn sẽ chọn một người để đọc thơ cho nha"
    ##
    menu doctho:
        "Nên đưa của mình cho ai đọc đây?"
        "Trọng Tiến":
         "Như cc, biến đi nhóc"
         "Lần tới mà viết như vậy là đuổi mày ra đó"
         "Nghe chưa?"
         jump chuong2_re
        "Văn Tiến":
         tien1 "Hmm.."
         tien1 "Cũng được đó chứ!"
         tien1 "Nói về cái đó à.."
         tien1 "Hay! Cố gắng phát huy"
         jump chuong2_re
        "Ngọc Trần":
         "Bảo Ngọc Trần" "Mình mới vào mà có biết đâu"
         banthan "...."
         jump chuong2_1
label chuong2_re:
    jump doctho
label chuong2_1:
    hide tien_shy
    show tien3:
        xalign 0.5
        yalign 0.5
    hide hatien
    hide bntblursed
    banthan "Hmm.."
    banthan "Hôm nay nhìn bạn tiến võ không được khỏe.."
    ##
    tien1 "À mà.."
    tien1 "Mình có thông báo.."
    tien1 "Trường mình sắp phải tổ chức lễ hội"
    tien1 "Và bọn mình.."
    tien1 "Phải tham gia lễ đó"
    banthan "Cái gì?"
    tien1 "Mình biết nó rất áp lực với các bạn.."
    tien1 "Và mỗi người phải lên sân khấu đọc thơ của mình cho mọi người nghe"
    hide tien3
    show hatien:
        xalign 0.5
        yalign 0.5
    tien2 "Mệt thật!"
    hide hatien
    with fade
    tien1 "Mình cũng vậy!"
    tien1 "Vì thông báo khá là đột xuất nên chắc các bạn phải.."
    tien1 "làm nhanh nhất có thể"
    tien1 "Và lần này các bạn phải làm về tết của việt nam.."
    tien1 "Và đó cũng sẽ là chủ đề cho buổi tối ngày hôm nay"
    tien1 "Các bạn nhớ về làm để mai mình gặp lại nhau"
    tien1 "Và cũng sẽ như ngày hôm nay"
    tien1 "Sẽ đọc thơ cho mọi người nghe"
    tien1 "Và ngày kế tiếp nữa sẽ là lễ hội, vào chủ nhật"
    hide tien_shy
    "Mọi người!"
    show hatien:
        xalign 0.25
        yalign 0.5
    show bntblursed:
        xalign 0.75
        yalign 0.5
    "Chúng ta sẽ làm cho xong nhe!"
    "Được thôi!"
    scene white
    "*Mọi người bắt đầu ra hành lang để chuẩn bị đi về*"
    "Thì"
    hide white
    scene hanhlang1 ##chua co
    banthan "Bạn Tiến ơi!"
    banthan "Đợi mình chút!"
    banthan "Bạn có bị làm sao không?"
    show tien_shy:
        xalign 0.5
        xalign 0.5
    tien1 "mình.."
    tien1 "mình không sao đâu"
    hide tien_shy
    banthan "Nhìn mặt bạn ấy đã khiến cho mình cảm thấy bất an.."
    show hatien
    show bntblursed
    banthan "Các bạn nghĩ sao?"
    "Bọn mình cũng thấy như vậy đó"
    "..."
    hide hatien
    hide bntblursed
    hide hanhlang1
    banthan "Thôi mình bây giờ cũng nên ra về"
    banthan "5 giờ chiều rồi.."
    banthan "Nhanh thật"
    scene truong
    ""
    hide truong
    show d2_1
    with fade
    "..."
    jump chuong3
label chuong3:
    stop music
    play music "sayo.mp3"
    "Chương 3: Bước hoặc"
    hide d2_1
    show bedroom1
    "..."
    "Vậy là một đêm nữa"
    "Haizz mệt ghê"
    "giờ lại phải viết về thơ nữa"
    "Hừmmm"
    "Bọn nó dặn viết về gì ta?"
    "Hình như đâu có đâu."
    "Mà thôi kệ"
    $ tho2 = renpy.input("Viết thơ của bạn:")
    $ tho2 = tho2.strip()
    "Rồi ok!"
    "giờ đi ngủ thôi"
    "à mà.."
    "mai là thứ 7 mà trường đâu mở lớp đâu"
    "thôi mai qua nhà bạn tiến chơi"
    ###
    scene black
    ""
    hide black
    scene white
    play sound "alarm.mp3"
    "Uì sáng rồi"
    "Nhanh thiệt"
    "Nên tới nhà bạn tiến không ta?"
    "Thôi tới luôn đi"
    hide white
    scene d2_1
    with fade
    hide d2_1
    with dissolve
    scene nhatien
    with fade
    "phía trước mình là một căn nhà hoạnh hiu"
    hide nhatien
    scene nhatiennight
    ""
    hide nhatiennight
    scene phongvantien
    banthan "Tiến?"
    banthan "Tiến ơi!"
    show tien3:
        xalign 0.5
        yalign 0.5
    tien1 "À"
    tien1 "Chào.."
    banthan "Có sao không vậy?"
    tien1 "Mình không sao đâu"
    tien1 "Chỉ là mình.."
    tien1 "Thấy hơi mệt thôi"
    "..."
    "Đúng là trước thềm lễ hội mọi người có vẻ"
    "Không được bình thường"
    banthan "À xém nữa mình quên mất"
    banthan "Thơ!"
    banthan "Bạn đã nhờ mình viết mình về cái này mà"
    banthan "Nè nè"
    banthan "Đọc thử đi"
    tien1 "hmm"
    tien1 "Cũng được đó"
    tien1 "Thêm một vài dòng nữa là tốt"
    tien1 "Mai mình sẽ khỏe trở lại"
    tien1 "Chắc luôn"
    tien1 "Nếu như mai mình không đến thì đừng đến nhà mình nhé"
    tien1 "Mình kiểu gì cũng sẽ tới thôi!"
    ".."
    show nhatien
    banthan "Vậy mình về trước nhé"
    "*Ra cổng*"
    "Tự nhiên mình có cảm giác.."
    "Rất bất an"
    "Thôi giờ về nhà"
    show d2_1
    ""
    hide d2_1
    show bedroom1
    with fade
    "Tệ thật"
    "Sao cái cảm giác này?"
    "Chuyện không lành vào ngày mai à?"
    "Mà thôi kệ"
    "Ráng ngủ sớm mai lên trường đọc thơ nữa.."
    jump chuongcuoi4
label chuongcuoi4:
scene black
stop music
"Chương cuối: Sự kết thúc trong vô vọng"
play music "just.mp3"
"Sao mình không ngủ được"
"Tệ thật"
hide black
scene white
play sound "alarm.mp3"
"TRỜI"
hide white
scene bedroom1
"Hết hồn"
"Mới có 4 giờ sáng mà"
"Tối qua mình có chỉnh gì đâu"
"giờ chắc mình hết ngủ được rồi"
hide bedroom1
scene nightstreet1
"Đường vắng thật"
"Thôi giờ đi luyện tập thơ chút"
"*Tự diễn thơ của mình trước kính*"
"Hành động nãy nhìn ghê rợn sao đó"
hide nightstreet1
scene d2_1
"ui"
"6 giờ sáng rồi nhanh thật"
"Tới trường thôi!"
hide d2_1
scene truong
""
scene hanhlang1
""
"Uả"
"Tiến đâu"
show hatien:
    xalign 0.5
    yalign 0.5
banthan "thấy tiến võ đâu không?"
tien2 "Mình không thấy nữa"
tien2 "Sắp tới giờ mà thằng đó chạy đâu rồi"
hide hatien
"..."
"Không lẽ"
hide hanhlang1
scene d2_1
"Tôi đã nhanh chạy ra cổng trường"
"Và ra đường D2"
show nhatiennight
"Tệ thật"
"Trễ giờ rồi"
banthan "CÓ AI Ở NHÀ KHÔNG"
"Không một ai trả lời lại"
"Tôi lên cầu thang và"
"Mở cửa thì.."
scene phongvantien
""
show tien_hang1:
    yalign 0.5
    xalign 0.5
".."
"CÁI"
""
scene black
with fade
"Tôi đã ngất xỉu ngay tại chỗ"
hide black
scene benhvien
""
banthan "mình"
banthan "đang ở đâu đây"
show tuyet:
    xalign 0.5
    yalign 0.5
"Tuyết Lưu" "Nãy thầy đi ngang thấy em xỉu ngay trên đường"
"Tuyết Lưu" "Trên người em có vết xước nữa, thầy nghĩ là em đã ngả từ trên lầu"
"Tuyết Lưu" "Có phải vậy không?"
banthan "umm"
banthan "đúng vậy"
banthan "KHOANG.."
banthan "Tiến!"
"Tuyết Lưu" "Tiến nào"
"Tuyết Lưu" "Võ Văn Tiến hả?"
"Tuyết Lưu" "Có chuyện gì xảy ra với em đó không?"
"Tuyết Lưu" "Nghe nói hôm nay em nó lên đọc thơ trước toàn trường mà"
"Tuyết Lưu" "giờ này chắc phải tới rồi chứ"
banthan "Không"
banthan "BẠN ẤY"
banthan "đã sục cu đie"
banthan "rồi thầy"
"Tuyết Lưu" "Cái gì?"
"Tuyết Lưu" "Không thể nào.."
"Tuyết Lưu" "Để thầy gọi 113"
hide benhvien
hide tuyetluu
scene black
"CHẾT TIỆT"
"TẠI SAO LẠI VẬY CHỨ"
"CÓ CÁCH NÀO KHÔNG?"
"CÓ CÁCH NÀO?"
"À"
"NẾU NHƯ MÌNH CÓ THỂ"
"QUAY NGƯỢC THỜI GIAN!"
jump credit
label credit:
    show bacho
    "Đến đây là kết thúc phần 1 của dd li tu ra tu re cờ club"
    "siêu phẩm của tác giả đỗ minh toàn"
    "nếu thấy hay nhớ cho bạn toàn 2k để bạn đó mua ly trà đá uống đỡ mệt sau 2h ngồi viết tiểu thuyết"
    "Phần tiếp theo sẽ được viết khi nào tác giả rảnh"
return
