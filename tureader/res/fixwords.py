from string import punctuation, whitespace

ranks = {'ศาสตราจารย์':['ศาสตรจารย์', 'ศาสตราจารย์', 'ศาสตร์ตราจารย์', 'Professor','ศ.(AIT)','ศ.(มจธ.)','ศ.(มทม.)','ศ.(มทส.)','ศ.(มวล.)','ศ.*','ศ.','ศ*','ศ'], 
         'ศาสตราจารย์เกียรติคุณ':['ศาสตราจารย์ กิตติคุณ'], 
         'รองศาสตราจารย์':["รองศาสตร์ตราจารย์", "Associate Professor",'รศ.'],
         "ผู้ช่วยศาสตราจารย์" : ['Assistant Professor','ผศ.','รด.','รศ.ดร.'],
         "ศาสตราจารย์ (พิเศษ)" : ["ศาสตราจารย์พิเศษ",'ศ.พิเศษ']}

def fixranks(word):
    return fixword(word, ranks)

phd = {'ดร.':['ดร','Dr.'] }

def fixphd(word):
    return fixword(word, phd)

status = {'เกษียณ':['กษ.','0','(เกษียณ)','เกษียณ (ต่ออายุ ราชการ)','เกษียณ (ต่อเวลา ราชการ)','เกษียณ (อาจารย์ พิเศษ)','เกษียณ วุฒิสมาชิก','เกษียน'],
          'ลาออก':['ลาออก (พำนักอยู่ อังกฤษ)', 'ลาออก(อยู่ต่างประเทศ)'],
          '':['จฬ.','มข.','์']}
def fixstatus(word):
    return fixword(word, status)

uni = {'มหาวิทยาลัยคริสเตียน':['ม.คริสเตียน'], 
       'จุฬาลงกรณ์มหาวิทยาลัย':['จฬ.', 'จฬ', 'นิติศาสตร์/จฬ.', 'นิติศาสตร์/จฬ','จุฬาลงกรณ์มหาวิทยาลัย','มจน','อักษรศาสตร์/จฬ'],
       'มหาวิทยาลัยรังสิต':['นิติศาสตร์/ม.รังสิต', 'ม.รังสิต', 'ม.รังสีต','ม. รังสิต'],
       'สถาบันเทคโนโลยีแห่งเอเชีย':['AIT'],
       'มหาวิทยาลัยศรีปทุม':['นิติศาสตร์/ ม.ศรีปทุม','นิติศาสตร์/ ม.ศรีปทุม','นิติศาสตร์/ ม.ศรีปทุม','ม.ศรีปทุม','มศป'],
       'มหาวิทยาลัยรามคำแหง':['นิติศาสตร์/มร','มร','นิติศาสตร์/มร','วิทยาศาสตร์/มร','มร','จฬ. โอน ไป มร','นิติศาสตร์/มร'],
       'สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง':['พระจอมเกล้าเจ้าคุณทหารลาดกระบัง','สจล'],
       'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ':['พระจอมเกล้าพระนครเหนือ','ครุศาสตร์ อุตสาหกรรมและ วิทยาศาสตร์/ สจพ','มจ','มจพ','สจพ'],
       'สถาบันรัชต์ภาคย์':['ม. รัชตํภาคย์'],
       'มหาวิทยาลัยฟาฏอนี':['ม. ฟาฏอนี','ม.ฟาฏอนี'],
       'มหาวิทยาลัยหอการค้าไทย':['ม. หอการค้าไทย','ม.หอ การค้า','ม.หอการ ค้าไทย','ม.หอการค้าไทย'],
       'มหาวิทยาลัยกรุงเทพ':['ม.กรุงเทพ'],
       'มหาวิทยาลัยเทคโนโลยีมหานคร':['ม. เทคโนโลยีมหานคร','ม.เทคโนโลยี มหานคร','ม. เทคโนโลยีมหานคร','ม.เทคโนโลยีมหา นคร','มทม','ม. เทคโนโลยีมหานคร','ม.เทคโนโลยี มหานคร'],
       'มหาวิทยาลัยกรุงเทพธนบุรี':['ม.กรุงเทพธนบุรี'],
       'มหาวิทยาลัยอีสเทิร์นเอเชีย':['ม.การจัดการ\nและเทคโนโลยี\nอีสเทิร์น','ม.อีสเทิร์นเอเชีย'],
       'มหาวิทยาลัยขอนแก่น':['ม.ขอนแก่น'],
       'มหาวิทยาลัยชินวัตร':['ม.ชิน วัตร','มข'],
       'มหาวิทยาลัยธุรกิจบัณฑิตย์':['ม.ธุรกิจ บัณฑิตย์','ม.ธุรกิจบัณฑิต','ม.ธุรกิจบัณฑิตย์','ม.ธุรกิจบันฑิต','มธบ','นิติศาสตร์/ม.ธุรกิจ บัณฑิตย์','ม. ธุรกิจบัณฑิตย์','มหาวิทยาลัยธุรกิจบัณฑิตย์','นิติศาสตร์/ม.ธุรกิจ บัณฑิตย์','ม. ธุรกิจบัณฑิตย์'],
       'มหาวิทยาลัยนราธิวาสราชนครินทร์':['ม.นราธิวาส ราชนครินทร์','มนร'],
       'มหาวิทยาลัยนอร์ท-เชียงใหม่':['ม.นอร์ท เชียงใหม่','ม.นอร์ท-เชียงใหม่'],
       'มหาวิทยาลัยนานาชาติเอเชีย-แปซิฟิก':['ม.นานาชาติ เอเชีย-แปซิฟิก'],
       'มหาวิทยาลัยปทุมธานี':['ม.ปทุมธานี'],
       'มหาวิทยาลัยพายัพ':['ม.พายัพ'],
       'มหาวิทยาลัยพิษณุโลก':['ม.พิษณุโลก'],
       'มหาวิทยาลัยรัตนบัณฑิต':['ม.รัตนบัณฑิต'],
       'มหาวิทยาลัยวงษ์ชวลิตกุล ':['ม.วงษ์ชวลิตกุล'],
       'มหาวิทยาลัยสยาม':['ม.สยาม'],
       'มหาวิทยาลัยสวนดุสิต':['ม.สวนดุสิต','มรภ. สวน ดุสิต','มรภ. สวนดุสิต','มรภ.สวนดุสิต'],
       'มหาวิทยาลัยหัวเฉียวเฉลิมพระเกียรติ':['ม.หัวเฉียว','ม.หัวเฉียวเฉลิม พระเกียรติ','ม.หัวเฉียวเฉลิมพระเกียรติ'],
       'มหาวิทยาลัยหาดใหญ่':['ม.หาด ใหญ่','ม.หาดใหญ่'],
       'มหาวิทยาลัยอัสสัมชัญ':['ม.อัสสัมชัญ'],
       'มหาวิทยาลัยเกริก':['ม.เกริก'],
       'มหาวิทยาลัยเกษมบัณฑิต':['ม.เกษม บัณฑิต','ม. เกษมบัณฑิต','ม.เกษม ปณฑิต','ม.เกษมบัณฑิต','ม. เกษมบัณฑิต'],
       'มหาวิทยาลัยเชียงใหม่':['ม.เชียงใหม่','มช','มนุษยศาสตร์และสังคมศาสตร์/มช'],
       'มหาวิทยาลัยเซนต์จอห์น':['ม.เซนต์จอห์น'],
       'มหาวิทยาลัยเอเชียน':['ม.เอเชียน','ม.เอเซียน'],
       'มหาวิทยาลัยเอเชียอาคเนย์':['ม.เอเชียอาคเนย์'],
       'มหาวิทยาลัยแม่โจ้':['ม.แม่โจ้'],
       'วิทยาลัยอาชีวศึกษาโปลีเทคนิคภาคตะวันออกเฉียงเหนือ':['ม.โปลีเทคนิค ตะวันออก เฉียง เหนือ'],
       'มหาวิทยาลัยเกษตรศาสตร์':['มก','วิศวกรรมศาสตร์/ มก'],
       'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี':['มจธ'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลศรีวิชัย':['มทร.\nธญบร','มทร. ศรีวิชัย','มทร.ศรีวิชัย'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลกรุงเทพ':['มทร. กรุงเทพ'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลตะวันออก':['มทร. ตะสันออก','มทร.ตะวันออก'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี':['มทร. ธัญ บุรึ','มทร. ธัญบุรี','มทร.ธัญบุรี','มภร.ธัญบุรี','มรภ.ธัญบุรี','มทร. ธัญ บุรึ'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลพระนคร':['มทร. พระนคร'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลรัตนโกสินทร์':['มทร. รัตน โกสินทร์','มทร. รัตนโกสินทร์'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลล้านนา':['มทร. ล้านนา','มทร.ล้านนา'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน':['มทร. อีสาน','มทร.อีสาน'],
       'มหาวิทยาลัยเทคโนโลยีราชมงคลสุวรรณภูมิ':['มทร.สุวรรณภูมิ'],
       'มหาวิทยาลัยทักษิณ':['มทษ'],
       'มหาวิทยาลัยเทคโนโลยีสุรนารี':['มทส'],
       'มหาวิทยาลัยนเรศวร':['มน','มนศ'],
       'มหาวิทยาลัยราชภัฏอุดรธานี':['มนุษยศาสตร์และ สังคมศาสตร์/มรภ. อุดรธานี','มรภ. อุดรธานี','มนุษยศาสตร์และ สังคมศาสตร์/มรภ. อุดรธานี','มรภ.อุดรธานี','อมรภ.อุดรธานี'],
       'มหาวิทยาลัยบูรพา':['มบ'],
       'มหาวิทยาลัยแม่ฟ้าหลวง':['มฟร','มฟล','สำนักวิชา นิติศาสตร์/มฟล'],
       'มหาวิทยาลัยมหาสารคาม':['มม','มมส','มมล','มม. (ลาออก'],
       'มหาวิทยาลัยราชภัฏกำแพงเพชร':['มรก. กำแพงเพชร','มรภ. กำแพงเพชร','มรภ. กำแพงเพชร','มรภ.\nกาแพง เพชร','มรก. กำแพงเพชร','มรภ.กาแพงพชร','มรภ.กาแพงเพชร','มรภ.กำแพง เพชร','มรภ.กำแพงพชร','มรภ.กำแพงเพชร','มรภ.ก้าแพง เพชร'],
       'มหาวิทยาลัยราชภัฏอุบลราชธานี':['มรก. อุบลราชธานี','มรภ.อุบลราชธานี'],
       'มหาวิทยาลัยราชภัฏเพชรบูรณ์':['มรก. เพชรบูรณ์','มรภ.เพชรบูรณ์','มรก. เพชรบูรณ์'],
       'มหาวิทยาลัยราชภัฏบ้านสมเด็จเจ้าพระยา':['มรภ.\nบ้านสมเด็จเจ้าพระยา','มรภ. บ้าน สมเด็จ เจ้าพระยา','มรภ. บ้านสมเด็จ','มรภ.บ้าน สมเด็จ เจ้าพระยา','มรภ.บ้านสมเด็จ','มรภ.บ้านสมเด็จ\nเจ้าพระยา','มรภ.บ้านสมเด็จ เจ้าพระยา','มรภ.บ้านสมเด็จฯ'],
       'มหาวิทยาลัยราชภัฏหมู่บ้านจอมบึง':['มรภ. จอมบึง','มรภ.จอมบึง','มรภ.หมู่บ้านจอมบึง'],
       'มหาวิทยาลัยราชภัฏจันทรเกษม':['มรภ. จันทรเกษม','มรภ.จันทรเกษม'],
       'มหาวิทยาลัยราชภัฎนครปฐม':['มรภ. นครปฐม','มรภ.นครปฐม'],
       'มหาวิทยาลัยราชภัฏนครราชสีมา':['มรภ. นครราชสีมา','มรภ.นครรราชสีมา','มรภ. นครราชสีมา','มรภ.นครราชสีมา'],
       'มหาวิทยาลัยราชภัฏนครสวรรค์':['มรภ. นครสวรรค์','มรภ.นครสวรรค์'],
       'มหาวิทยาลัยราชภัฏบุรีรัมย์':['มรภ. บุรีรัมย์','มรภ.บุรีรัมย์'],
       'มหาวิทยาลัยราชภัฏพระนคร':['มรภ. พระนคร','มรภ.พระนคร'],
       'มหาวิทยาลัยราชภัฏพระนครศรีอยุธยา':['มรภ. พระนคร ศรีอยุธยา','มรภ. พระนครศรีอุยธยา','มรภ.พระนครศรีอยุธยา'],
       'มหาวิทยาลัยราชภัฏพิบูลสงคราม':['มรภ. พิบูลสงคราม','มรภ.พิบูลสงคราม'],
       'มหาวิทยาลัยราชภัฏภูเก็ต':['มรภ. ภูเก็ต','มรภ.ภูเก็ต'],
       'มหาวิทยาลัยราชภัฏราชนครินทร์':['มรภ. ราช- นครินทร์','มรภ.ราชนครินทร์'],
       'มหาวิทยาลัยราชภัฏวไลยอลงกรณ์':['มรภ.ว ไลยอลงกรณ์','มรภ. วไลยอลงกรณ์','มรภ.วิไลย อลงกรณ์','มรภ.วไลยอลงกรณ์','มรภ.วไลยอลงกรณ์มรภ.วไลยอลงกรณ์','มรภ.วไลยอลงกรณ์ในพระบรมราชูปถัมภ์','มรภ. วไลยอลงกรณ์'],
       'มหาวิทยาลัยราชภัฏสกลนคร':['มรภ. สกลนคร','มรภ.สกลนคร','มรภ. สกลนคร'],
       'มหาวิทยาลัยราชภัฏสงขลา':['มรภ. สงขลา','มรภ.สงขลา'],
       'มหาวิทยาลัยราชภัฏสุราษฎร์ธานี':['มรภ. สุราษฎร์','มรภ.สุราษฎร์ธานี'],
       'มหาวิทยาลัยราชภัฎสุรินทร์':['มรภ. สุรินทร์'],
       'มหาวิทยาลัยราชภัฏเทพสตรี':['มรภ. เทพสตรี','มรภ.เทพสตรี'],
       'มหาวิทยาลัยราชภัฏอุตรดิตถ์':['มรภ. อุตรดิตถ์','มรภ.อุตรดิตถ์'],
       'มหาวิทยาลัยราชภัฏเชียงราย':['มรภ. เชียงราย','มรภ.เชียงราย','มรภ.เชียงราย'],
       'มหาวิทยาลัยราชภัฏเชียงใหม่':['มรภ. เชียงใหม่','มรภ.เชียงใหม่'],
       'มหาวิทยาลัยราชภัฏเพชรบุรี':['มรภ. เพชรบุรี','มรภ. เพชรบุรึ','มรภ.เพชรบุรี'],
       'มหาวิทยาลัยราชภัฏเลย':['มรภ. เลย','มรภ.เลย'],
       'มหาวิทยาลัยราชภัฏกาญจนบุรี':['มรภ.กาญจนบุรี','มรภ.กาญจบุรี'],
       'มหาวิทยาลัยกาฬสินธุ์':['มรภ.กาฬสินธุ์'],
       'มหาวิทยาลัยราชภัฏชัยภูมิ':['มรภ.ชัยภูมิ'],
       'มหาวิทยาลัยราชภัฏธนบุรี':['มรภ.ธนบุรี'],
       'มหาวิทยาลัยราชภัฎมหาสารคาม':['มรภ.มหาสาร คาม','มรภ.มหาสารคาม'],
       'มหาวิทยาลัยราชภัฏรำไพพรรณี':['มรภ.รําไพ พรรณี','มรภ.รําไพพรรณี'],
       'มหาวิทยาลัยราชภัฏลำปาง':['มรภ.ลาปาง','มรภ.ลำปาง','มรภ.ลําปาง'],
       'มหาวิทยาลัยราชภัฏศรีสะเกษ':['มรภ.ศรีสะเกษ'],
       'มหาวิทยาลัยราชภัฏสวนสุนันทา':['มรภ.สวนสุ,ผันทา','มรภ.สวนสุนันทา'],
       'มหาวิทยาลัยสุโขทัยธรรมาธิราช':['มลธ','มสธ','สาขาวิชา นิติศาสตร์/มสธ'],
       'มหาวิทยาลัยวลัยลักษณ์':['มวล'],
       'มหาวิทยาลัยศิลปากร':['มศก','มสก'],
       'มหาวิทยาลัยศรีนครินทรวิโรฒ':['มศว'],
       'มหาวิทยาลัยสงขลานครินทร์':['มอ','มอ. (ปัตตานี'],
       'มหาวิทยาลัยอุบลราชธานี':['มอบ'],
       'วิทยาลัยเซนต์หลุยส์':['ว.เซนหลุยส์'],
       'สถาบันเทคโนโลยีไทย-ญี่ปุ่น':['ส. เทคโนโลยี ไทย-ญี่ปุ่น','ส.เทคโนโลยี ไทย-ญี่ปุ่น'],
       'สถาบันการจัดการปัญญาภิวัฒน์':['ส.การจัดการปัญญาภิวัฒน์','ส.การรัดการ ปญญาภิรัฒน์'],
       'สถาบันวิชาการปัองกันประเทศ':['สปท'],
       'สถาบันพัฒนาบุคลากรท้องถิ่น':['สพบ'],
       'มหาวิทยาลัยธรรมศาสตร์':['นิติศาสตร์/มธ','มธ','มธ.','มธ. (ศูนย์รังสิต','มธก','ม.ธรรมศาสตร์','วารสารศาสตร์และการสื่อสาร\nมวลชน/มธ'],
       'มหาวิทยาลัยมหิดล':['มหาวิทยาลัยมหิดล','MU','มม','มม.','มม. (ลาออก'],
       'สถาบันบัณฑิตพัฒนบริหารศาสตร์': ['สถาบันบัณฑิตพัฒนบริหารศาสตร์','นิด้า','สพบ.','NIDA'],
       'มหาวิทยาลัยราชพฤกษ์': ['มหาวิทยาลัยราชพฤกษ์','RPU','มรพ.']}
def fixuni(word):
    return fixword2(word, uni)


def fixword2(word, vocab):
    word = word.strip(punctuation + whitespace)
    for key, value in vocab.items():
        if word in value:
            return key
    return word


def fixword(word, vocab):
    word = word.strip()
    for key, value in vocab.items():
        if word in value:
            return key
    return word