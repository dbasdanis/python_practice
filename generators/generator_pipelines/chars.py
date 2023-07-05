data = [
    "zoo length wrong shinning mathematics shoulder stage example weak roll found evidence species born grain further offer whose stay rope provide everyone ice pound",
    "peace forty almost myself pride roar disappear harbor contain nest expression lost cost happy select jack leader cloth physical farmer rising army every element",
    "onto oxygen thick process until thin feathers personal fruit worse yes eat shot poet feet tales beneath steam thread know you worry best herd",
    "tall serious creature weather close lie grabbed orange past radio chose fact cow public act perfect dirty pot cup was cake cap fix secret",
    "hunter elephant kids against thought becoming source those prevent behind solution suddenly wolf duck long construction thou information closely letter together wet distant show",
    "lonely bow dead effort pleasure arrange dirty torn series what speech individual congress yes solution came daughter throughout business gather come learn cow using",
    "fact thy properly talk statement tropical education serve composed parent unit die door older pull should by almost blue weak found primitive oil pleasure",
    "breath wind unless sister scared sudden selection neighbor direction ground tropical hurt fell us furniture right card shinning guard than paid lion you quietly",
    "round chain act forget trouble magic angry now instance command are queen bowl captain work deep underline vote also foreign service struggle managed complex",
    "favorite mood student mouth wall event settle compound chamber stream floor power season tightly happy require sang radio else ago young rapidly damage clear",
    "hole explain handle early here bush nest cotton does angle clearly wind fruit slightly wrong signal sink needle exact island face married party general",
    "moon frequently complete essential deep complex way dead lot amount lesson grown pride meat knowledge score remove nearly ever tonight automobile decide us won",
    "wood could press wife lay ten blow area dug mental pale glass clothes board six anybody everything apart will other pride ran straight living",
    "vessels excellent traffic pupil choose jungle supply slight trap animal simplest burst same forty fighting away truth sit ill weigh former familiar eaten common",
    "silver case ahead barn whispered kind from breath cave fill forest addition cat manner train children greater accept unusual television but jack fighting went",
    "attack correctly getting tune think joined bent shoulder according roof swept yes managed visit harder particles pole feet yourself knew warn plates ourselves brown",
    "stomach seldom trail pure tool river captured gray farm she equator fight row laid observe flat better look brass cool different why book south",
    "metal church string alphabet nearly number record depth outline remain for where sugar arrange twenty poet struggle body particular after tell mix agree scientific",
    "peace mass forty colony dress it shelter sides printed shout pupil energy law nature also person lake chance drawn noon though crop meant although",
    "dull recent road tone ask exercise almost rice tried log environment part circle enemy seen business parts own stretch problem classroom win done glass",
]

strip_ws = (string.replace(" ","") for string in data)
len_str = (len(s) for s in strip_ws)
less_than = (num for num in len_str if num < 130)
print(list(less_than))