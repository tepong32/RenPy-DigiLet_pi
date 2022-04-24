# the remake part, obviously...duh?

label theRemake:
    # scene bg ricefields
    scene black with fade
    show neutral with dissolve
    "Okaaaaaaaaaay! So eto na nga! haha Ayos na ha? TheRemake na to. \nAndito yung effort ko talaga e."
    show ehe
    "Yung bracelet na tig-20, humanap na lang tayo some other time. \nWorth 30 na ung bibilhin ko for you para mas okay. Hehe JK!"
    hide ehe
    "Game na! Q&A! ;)"
    jump q1

### Question #1
label q1:
    "Do you remember when we first held hands?"

    show neutral at left
    menu:
        "Syempre naman!":
            jump q1_yes

        "Uhhh... (\"Hindi\" in Pinky's tone)":
            hide neutral
            jump q1_no

    label q1_yes:
        $ menu_flag = True
        # user input placed here
        python:
            date1 = renpy.input("Kailan? (mmddyyyy)")
            date1 = date1 # "07122018"
        if str(date1) == ("07122018"):
            jump q1_done
        else:
            "Awwwwww. Mahirap ba to? Need a clue? \n2nd week of July. ;)"
            jump q1_yes

    label q1_no:
        $ menu_flag = False
        show c_haist at left
        with fade
        "Bat mo nga naman tatandaan di ba?"
        "Sagutin ko na rin para hindi naman ako mapahiya. \n07122018"
        # hide c_haist
        with fade
        jump q1_done

    label q1_done:

        if menu_flag:
            hide neutral
            show c_ha with flashbulb
            "Haneeeeppp! So, tinandaan mo rin? I'm... touched."
            hide c_ha
            show c_happy
            "Or hinulaan mo na lang ung dates sa 2nd week? haha!"
            hide c_happy with dissolve
            # show bus screen here....bat ayaw gumana!?
        else:
            show bus at right behind c_haist with slowdissolve
            "Well, anyway, hindi naman yun mahalaga. What's important is now you know. \nTechnically, that was 13 kase madaling araw na..."
            "...sa bus. di ba?"
            hide c_haist
            show c_ehe at left with dissolve
            "I would love to remember as much details as I could kaso di ko matandaan ung name ng bus. LOL"
            hide bus with dissolve
            show sanmig at left with dissolve
            pause 0.5
            show cheetos at right with dissolve
            pause 0.5
            hide sanmig
            hide cheetos with dissolve

            "Remember the beer? The spicy cheetos? The field? The rain?"
            hide c_ehe with dissolve
            ""
            show push at right with dissolve
            show c_ehe at left with dissolve
            pause 1.0
            hide c_ehe
            show c_happy at left
            "Ay oo nga! HAHAHAHA!"
            "Mamaya mo na alalahanin ung pagtutulak mo, Pi! HAHAHA! SORRY NA KASI E!"
            hide push with dissolve
            "Sabi naman sayo, at least, sakin mo lang na-experience un!"
            hide c_happy
            show c_poker at left with dissolve
            "Setting that \"pagtutulak\" aside,... (ibahin ko na agad topic. hehe)"
            "That night was when I actually first wanted to kiss you..."
            hide c_poker
            show c_ehe with dissolve
            "...and I'm not telling just a kiss on the cheeks. I was looking at your lips back then. Honestly. haha"
            hide c_ehe
            show c_poker at left with dissolve
            "Same as nung andun tayo kela Jude. I was looking... \njust looking though."
            "I mentioned this din after nung kela Jude di ba? Pero that first night we were together..."
            "...at the field"
            "...umuulan?"
            hide c_poker
            show c_neutral with dissolve
            "...gustong-gusto kitang halikan."
            "I just don't know if I was afraid or I was just thinking na hindi pa yun ung oras...Maybe both?"
            hide c_neutral
            show c_haist at left with dissolve
            "That may be a perfect place but definitely not a perfect timing...and I was right."
            "Galing ko talaga sa mga ganun e!"
            "I'm somehow glad that I hesitated and my hesitaion won."
            hide c_haist
            show closeup at left with dissolve
            "ANYWAAAAAAAAY...NEXT!"
            jump q2

### Question #2
label q2:

    python:
        bday = renpy.input("When was Eliz' first birthday celebrated? (mmddyyyy)")
        # "07282018"
    if str(bday) == ("07282018"):
        jump q2_done
    else:
        "Clue? Same month (last week), same year. XD"
        jump q2

    label q2_done:
        hide closeup
        show c_happy at left with dissolve
        "Yoooonnn! Berigud! haha"
        hide c_happy
        show c_poker at left
        "Skipping the party details, we moved to Jude's place for..."
        hide c_poker
        show c_ehe at left with dissolve
        "uh...movies? LOL Whatever that was called."
        "We ate the giveaway cakes from the party, tried to find a good movie to watch, Jude and I drank a little GinBu... haha"
        hide c_ehe
        show c_neutral at left with dissolve
        "My fear was gone for a moment (or may have gone away for the moment we were in there, at least) and I held your hands again...in front of them."
        hide c_neutral
        show c_happy at left
        "YIIIIIEEE! <3"
        ""
        ""
        "AYYIIIIIIIEEEEEEE!! HAHAHA"
        "I was tipsy pero feeling ko okay lang. Okay lang naman di ba? I mean we're all friends naman doon."
        hide c_happy
        show c_poker at left
        "Besides, matagal naman na silang boto sayo for me."
        "No kidding. I was often asked pag magkikita-kita kame (kahit wala ka):"
        ""
        hide c_poker
        show c_neutral at right with dissolve
        "\"Bakit di na lang si Pinky?\""
        hide c_neutral
        show c_ehe at left with dissolve
        "Tinatanong din naman nila yan pag magkasama tayo di ba? Tinatanong din nila kahit hindi kapag nababanggit kita. Ganun."
        "E bakit nga ba?? hahaha"
        hide c_ehe
        jump q3

### Question #3
label q3:
    show neutral at left with dissolve
    "You wanna know why?"
    menu:
        "Syempre naman!":
            jump q3_yes

        "Wag na lang siguro... (in Pinky's tone)":
            hide neutral
            show c_ehe with fade
            "Di nga sabi ako papayag na NO dito...sayang effort ko, anu ka baaaaaa? HAHAHA"
            "Uulit lang to. Kailangan mag-yes ka... Click YES! haha"
            hide c_ehe with dissolve
            jump q3

    label q3_yes:
        hide neutral
        show neutral2 with dissolve
        "GOOD! Warning: YOU proceeded at your own risk. (HAHAHAHA! Feeling ko ang witty ko sa disclaimer na to. shet!)"
        "You may either hate or admire what you'll come to know after this."
        "This is where things get a little bit exciting. *insert devilish smirk*"
        hide neutral2 with dissolve
        show closeup with dissolve
        "I actually had this idea na: \n\"Ayokong maging first boyfriend mo\"."
        hide closeup
        show c_poker
        "Seriously...ayoko lang. Why? "
        "Gusto ko lang fair. You're not my first. I don't want to be your first either."
        "Munggago no?"
        "\"Fair\" in a sense na maybe, just maybe, you can then understand why I held on to the first relationship I had. You need to understand what I went through."
        "It's different from what you experienced pero somewhat similar in a way na they got the best of us...and the best of us just got thrown away."
        "The misery of getting your heart broken from a commitment? Saket di ba?"
        hide c_poker
        show c_ehe
        "But don't get me wrong. I did not think about that because I want you to suffer (\"suffer more\" should be the term here kase I made you suffer before na...)."
        "I wanted you to understand. And by now, I definitely think na you fully understand it na. Tama?"
        "HEEEYY! I know I sounded very confident dun sa early part nitong thought na sinasabi ko. haha 'I don't want to be your first'? Damn! So, sure akong magbe-break kayo ng first mo? Na magiging tayo?? HAHAHAHA!"
        "Ang yabang ko di ba? Ang assuming. But honestly, yeah. I honestly think I have the slightest chance pa rin naman e... chance. Right?"
        hide c_ehe
        show c_haist
        "Well, for the sake of this 'letter', pabayaan mo na lang. Let it go, let it go. haha "
        "If I am overall, totally and completely wrong, then...Okay lang din naman. Sabihin na lang natin na that's what I thought when I came up with this idea of \"fairness\"."
        hide c_haist
        show c_poker
        "Yung fair as in: meron tayo parehong pagkukumparahan. Walang maisusumbat ba if magkaroon ng kung ano mang away or tampuhan. Ganun..."
        "In a positive way, I just don't like the idea of me having someone prior tapos ikaw, wala."
        "Pero seryoso...di sapilitan 'to. Okay lang kahit ano. Sabi ko nga lage, pwede ka gumanti. Tapos feeling ko di rin naman na ko ganun maaapektuhan."
        hide c_poker
        show c_ehe
        "I mean...uh? Pano ba to? haha Di naman sa di ako seryoso...Lagi naman akong seryoso pagdating sa mga ganito pero siguro I just don't want to put my all pa until okay na. Okay ka na...Okay na tayo. Ganun."
        "If di magiging tayo, edi wow. HAHAHA deeehh..Promise okay nga lang. Feeling ko kaya ko na rin ung ginawa mo like remaining friends even after all that has happened: Maturity."
        hide c_ehe
        show c_neutral
        "I am well aware and very precautious na rin pagdating dito. Tengene mesheket e. Teteeng mesheket debe? :D "
        "Life is what happens while we're busy making our excuses. (wow? sa kanta ng simple plan yan galing...pero ano'ng konek?)"
        "Wala. Maybe I just wanted you to know that. I think I brought this up on a conversation we had before din naman...tapos di ko tinuloy. Sabi ko may better timing. Eto yun. ;)"
        hide c_neutral with dissolve
        hide c_haist
        show neutral2 at right with fade
        "So, ayun! Now you know. Ayos ba? Ganda ng revelation ko no? Well-thought-out slash well-planned and executed. Na-predict? LOL"
        "...and that's that! Ngayon...Ano gagawin naten? HAHAHA"
        "Sa tingin mo, ano?"

        jump q4

### Question #4
label q4:
    "Should we take this to the next level na? "
    "Okay ka na ba? "
    "This time, for real...as adults...ano? "
    "Honestly, I've always wanted to have a girlfriend na rin naman...all those years. Ulit... Just that wala akong kasundo...AS MUCH AS YOU DO. So I waited..."
    "HAHA! Specialty ko nga yata talaga yung patience...yung waiting, specifically. My goodness! "
    "SO! Ano?? Required ang sagot dito sa next dito. And I setup the program to send me the answer to this question. HAHAHAHA! (Ang galing ko na, shet!)"
    "Moment of truth kase tinuloy mo hanggang dito e. But unlike all the other questions thrown at you before, there will be no re-try's after this question."
    "Press enter after each line carefully."
    "Breathe..."
    "Inhale..."
    "Exhale..."
    "Ready? "
    "Here we go: "
    "Unexpected Runtime Error. Exiting program."
    ""
    ""
    hide neutral2
    show c_happy at right with dissolve
    "Joke lang! Eto na talaga..."

    label q4_1:
        "Will be my girlfriend, Pinky?"
        menu:
            "Yes.":
                hide c_happy
                jump q4_1_yes

            "No":
                hide c_happy
                show c_ehe at right with dissolve
                jump q4_1_no

        label q4_1_yes:
            hide neutral
            show ha at right with flashbulb
            hide ha
            show smile at right
            "ORAAAAYYYYTTT! EPEKTIB! MWAHAHAHAHAHAHA!"
            "Pero joke lang yung sinabi ko. Di ko malalaman sagot dito. Di pa ko ganun kagaling no."
            "Basic pa lang tong alam ko at iniapply dito. That was just a test."
            "But I want you to think about it really hard...for if we continue this setup, I'm really going to ask that same question to you. And of course..."
            hide smile
            show c_happy with flashbulb
            "YOU CAN'T SAY NO. hahahaha!"
            "Yeah, nah. I will not accept a NO."
            "I won't ask that if I feel na you won't go for it naman din. Marunong ako makiramdam..."
            "So, if you will go for it, wag mo iparamdam na hinde. Kundeee...aynako. Sayang ako sige ka. ;)"
            hide c_happy
            jump pre_ending

        label q4_1_no:
            hide neutral
            show c_ehe with flashbulb
            "Okay. I somehow expected that due to the circumstances you are in. I understand naman. Thanks for being honest."
            "Still, this will run the ending script. ;)"
            "...and here it goes..."
            "take note: this specific line was made on October 3rd 2018. If you are seeing this, that means you answered no to the last question. Either right away or you tried it again, you answered no."
            "Honestly, eto na lang ung binago ko dito. This was all done before you said: Don't do this anymore chuchu. haha'"
            "Keribum. I just wanted to insert here that I'm still thankful for the chance to make-up with you."
            "Maybe also thankful for not letting me hurt you again? \nWe cannot tell since it did not happen."
            "But please be reminded na pwede mo pa rin ako ayain. haha Lilibre mo pa ko ng kape di ba?? May pupuntahan pa tayo ng nakamotor? Di ba?? :)"
            hide c_ehe
            jump pre_ending

        label pre_ending:
            show c_neutral with dissolve
            "Osya. Masyado nang mahaba eto na talaga ung ending script..."
            ""
            ""
            hide c_neutral
            show c_happy
            "weeeeeyyyyytttt!"
            "Somewhere along the line, during the days I was typing slash coding this, naisip ko idagdag ung mga darating pa nating usapan..."
            "or maybe kung ano man yung mga mapapansin ko pa na pwede ko ilagay dito."
            "Here they are:"
            jump add_ons

    label add_ons:
        #any other thing na gusto mo ilagay pampahaba. Oh well, pag nakita ni Pinky to, aynako. Kikiligin yun e. HAHAHA! (mababasa mo kaya to?)
        "Wo0o0o0o0oh! So ayon, eto yung mga feel ko idagdag. You can call this bloopers or behind the scenes, I guess, if ikukumpara mo sa movies? hehe"
        "If you'll try to look at how I coded this, you can check the lowest part slash ending of the script."
        "You'll see how I created/named the flow. PLUS: comments ko while I was making this. haha"
        "They may be not-so-worth-it din so I suggest na wag na lang. Eto na yun e. ;) "
        "intro"
        "thePast"
        "theRemake"
        "add_ons"
        "disclaimer"
        "ending"
        "BTW, today was August 26, 2018 habang tinatype ko tong add_ons na to. I just wanted to commend you for really knowing me OH SO WELL. :D"
        "Wala lang. Napansin ko sa usapan naten...yung sabi ko: \"sana midshift, sana midshift.\", ang reply mo was: \"tignan naten kung malakas ka sa universe.\""
        "I belive you know...tama ba?"
        "I'm not a fan of religion...not anymore, at least. Or to further that (ano daw?? can't find the term): not as much as I used to. Do you want to know why? "
        "Wag na. haha Basta ayos na ayos ako na alam mo yun. You deserve to be praised for noticing that. ;) "
        ""
        "---September 9---"
        "Second weekend after ko magstart ng work. We watched The Hows of Us noong:  "
        "October 31 yata. HAHAHA! Oo noon un. Wala lang. Isiningit ko lang dito para if ever babalikan mo too in the future,..."
        "alam mong ang sexy sexy mo nung araw na yun. hart hart hart <3"
        "Feeling ko wala na kong masyadong maidaragdag dito kase nga nagwowork na ko tapos by the end of this month, before your birthday, e may gala ka."
        "Okay lang naman. Haha I just hope na hindi masyadong matagal after ng bday mo ung day na magkikita tayo kase may inilagay ako sa bandang unahan nito di ba about dun sa lakad mo? haha"
        "So, ayun na! If may susunod na movie tayong papanuorin, sabihan mo lang ako in advance. :)"
        jump disclaimer

    label disclaimer:
        "Before the ending script runs, I just want you to know na...you don't have to give me a feedback about this if you don't want to."
        "I just gave you a heads-up of what will come to you should we further continue this setup. LOL I'm dead serious here."
        "...and being that dead serious: say, honestly, do you think we'll work out? Try to think hard about it...even just for this instance."
        "hmm?"
        "Anyway, itatanong ko talaga sayo yung kanina. Sooner or later. Actually,...yeah. Pwede mo na rin namang sagutin right at this moment kung feel mo na e. Hehe"
        "Magload ka tapos tawagan mo ko. HAHAHA Kuripot neto sa load. Daig mo pa ko e anlaki-laki ng sahod mo. HAHA"
        "So, sya, ending script na. TALAGA. ;)"
        jump ending

    label ending:
        "So, I'm wrapping this up na..."
        "I hope I made this as interactive as it can be, as conversational as it can be. And just a heads up, maybe I can't make something as grand (or grander) than this in the future na. I mean, hello? Ano pa yung sasabihin ko di ba? Pwede na ngang pang proposal tong idea na to e! HAHA"
        "Seryoso, totoo naman di ba?"
        "Naisingit ko lang. :)"
        "So...Going back to what this was for:"
        " Happy, Happy Birthday! Siguro nasa malayo ka ngayon kase sabi mo nagbook ka na ng birthday gala mo e. Haha! Ienjoy mong mabuti yan. Have a safe trip back here."
        ""
        ""
        ""
        ""
        ""
        "Ano pa?"
        "Bakit pindot ka pa ng pindot??"
        "Gusto mo pa? HAHAHAHA!"
        "Lakas mang-inis e? Wala naaaaaaaa! Wala na kong masabi. Kaloka ka. Ganda ng love letter ko sayo no? Naenjooly mo ba? AMINIIIIIINNN!"
        "This is another something na I bet, sakin mo lang maeexperience...bukod dun sa pagtutulak ng multicab! hahaha #Effort! WOo0o0o0o0oh!"
        "Pano? Sige na, ingat ka...Get back here."
        "I love you."
        "Disclaimer number two:  "
        "I have always loved you naman. Alam na alam mo yan. haha There are different kinds of love, di ba?"
        "This \"I love you\"..."
        "It's somewhere near the defining line of being my closest female friend and being my special someone."
        "Honestly, I can't determine yet. Epekto ng pagiging single for so long? I don't know."
        "I'm bringing myself down on this e no? Habit ko na ung ipahamak sarili ko thru being honest."
        "Well, that's just how I roll. Gusto ko open lahat para walang sisihan sa huli."
        "Kainis no? Sinira ko pa. hahahaha Sorry na. Sanay ka naman na sa'kin di ba? \nSa depressing personality ko..."
        "Basta I love you, Pinky."
        "Bahala ka na mag interpret nyan. Yan na yun. TIME!"
        "---end"
