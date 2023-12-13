import datetime

sample_test_data = [
    {
        "children": [],
        "created_at": datetime.datetime(2023, 11, 13, 14, 10, 9),
        "email": "lisa93@example.com",
        "firstname": "Joseph",
        "password": "!q62J8^sYb",
        "role": "user",
        "telephone_number": "756037486",
    },
    {
        "children": [
            {"age": 12, "name": "Steven"},
            {"age": 18, "name": "Christine"},
            {"age": 6, "name": "Rachel"},
        ],
        "created_at": datetime.datetime(2023, 4, 12, 22, 7, 59),
        "email": "hunter96@example.org",
        "firstname": "Shannon",
        "password": "sD3NddkqB*",
        "role": "admin",
        "telephone_number": "121975731",
    },
    {
        "children": [
            {"age": 14, "name": "Jessica"},
            {"age": 11, "name": "Megan"},
            {"age": 9, "name": "Michael"},
        ],
        "created_at": datetime.datetime(2023, 11, 10, 9, 52, 49),
        "email": "weisskristina@example.net",
        "firstname": "Steven",
        "password": "9T1zNeAN(2",
        "role": "user",
        "telephone_number": "691250247",
    },
    {
        "children": [
            {"age": 1, "name": "Tracy"},
            {"age": 1, "name": "Joseph"},
            {"age": 8, "name": "Whitney"},
        ],
        "created_at": datetime.datetime(2023, 1, 18, 20, 39, 19),
        "email": "ashleyschwartz@example.org",
        "firstname": "Mark",
        "password": "I35_C9id^P",
        "role": "admin",
        "telephone_number": "967426092",
    },
    {
        "children": [
            {"age": 4, "name": "Sheila"},
            {"age": 12, "name": "Laurie"},
        ],
        "created_at": datetime.datetime(2023, 4, 28, 11, 35, 28),
        "email": "halemisty@example.net",
        "firstname": "Brianna",
        "password": "_r1CEmbZHe",
        "role": "admin",
        "telephone_number": "505400027",
    },
    {
        "children": [{"age": 15, "name": "John"}, {"age": 13, "name": "Brian"}],
        "created_at": datetime.datetime(2023, 4, 5, 3, 50, 42),
        "email": "erik91@example.org",
        "firstname": "Jeffrey",
        "password": "25pEhHfx$Y",
        "role": "user",
        "telephone_number": "854869516",
    },
]


clean_data = [
    {
        "children": [{"age": 11, "name": "Rebecca"}, {"age": 17, "name": "Christie"}],
        "created_at": datetime.datetime(2023, 5, 15, 21, 57, 2),
        "email": "jwilliams@example.com",
        "firstname": "Russell",
        "password": "4^8(Oj52C+",
        "role": "admin",
        "telephone_number": "817730653",
    },
    {
        "children": [{"age": 3, "name": "Andrew"}, {"age": 13, "name": "Nicholas"}],
        "created_at": datetime.datetime(2023, 11, 13, 1, 28, 53),
        "email": "briancollins@example.net",
        "firstname": "Dawn",
        "password": "R9AjA5nb$!",
        "role": "admin",
        "telephone_number": "717279856",
    },
    {
        "children": [{"age": 11, "name": "Frank"}],
        "created_at": datetime.datetime(2023, 6, 25, 6, 56, 34),
        "email": "billy59@example.com",
        "firstname": "Bryan",
        "password": "%ML4fCTmiz",
        "role": "user",
        "telephone_number": "242024650",
    },
    {
        "children": [{"age": 8, "name": "Rachel"}, {"age": 13, "name": "Bradley"}],
        "created_at": datetime.datetime(2023, 9, 27, 15, 27, 18),
        "email": "johnperry@example.com",
        "firstname": "Sarah",
        "password": "bd6GvDNA!+",
        "role": "admin",
        "telephone_number": "318506164",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 11, 3, 0, 23, 19),
        "email": "fpage@example.net",
        "firstname": "Teresa",
        "password": "hJ@2Kbg2tF",
        "role": "admin",
        "telephone_number": "522263177",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 9, 26, 13, 14, 3),
        "email": "sherrystein@example.com",
        "firstname": "Gregg",
        "password": "nO6ySyLH&7",
        "role": "user",
        "telephone_number": "707470796",
    },
    {
        "children": [{"age": 2, "name": "Shirley"}, {"age": 1, "name": "Martin"}],
        "created_at": datetime.datetime(2023, 4, 7, 13, 1, 16),
        "email": "janice79@example.net",
        "firstname": "Ashley",
        "password": "kj5JYvkv(6",
        "role": "user",
        "telephone_number": "135086990",
    },
    {
        "children": [
            {"age": 13, "name": "Keith"},
            {"age": 3, "name": "Sheila"},
            {"age": 5, "name": "Trevor"},
        ],
        "created_at": datetime.datetime(2023, 4, 19, 22, 54, 52),
        "email": "thompsonrobert@example.com",
        "firstname": "Emily",
        "password": "4_iLvqWu^0",
        "role": "admin",
        "telephone_number": "735760245",
    },
    {
        "children": [{"age": 4, "name": "Andrew"}, {"age": 13, "name": "James"}],
        "created_at": datetime.datetime(2023, 3, 2, 16, 37, 42),
        "email": "esexton@example.net",
        "firstname": "Patricia",
        "password": "eFaU94Jc#&",
        "role": "admin",
        "telephone_number": "636162531",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 9, 19, 2, 36, 39),
        "email": "cherrera@example.com",
        "firstname": "Gregory",
        "password": "6uH#d)l^^_",
        "role": "admin",
        "telephone_number": "700851384",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 1, 29, 3, 18, 13),
        "email": "hstephenson@example.org",
        "firstname": "Betty",
        "password": "W_14V1rdyp",
        "role": "admin",
        "telephone_number": "630570268",
    },
    {
        "children": [
            {"age": 11, "name": "Christopher"},
            {"age": 12, "name": "Suzanne"},
            {"age": 3, "name": "Joshua"},
        ],
        "created_at": datetime.datetime(2023, 3, 22, 22, 40, 41),
        "email": "annakane@example.com",
        "firstname": "Theresa",
        "password": "df#vDs!#$6",
        "role": "admin",
        "telephone_number": "513112467",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2022, 11, 25, 2, 19, 37),
        "email": "opoole@example.org",
        "firstname": "Justin",
        "password": "+3t)mSM6xX",
        "role": "admin",
        "telephone_number": "678762794",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 4, 2, 15, 57, 34),
        "email": "woodsjerry@example.com",
        "firstname": "Patricia",
        "password": "z2Y%0Hbcsi",
        "role": "user",
        "telephone_number": "823816375",
    },
    {
        "children": [{"age": 18, "name": "Anna"}],
        "created_at": datetime.datetime(2023, 10, 10, 21, 3, 45),
        "email": "josenavarro@example.net",
        "firstname": "Hannah",
        "password": "yw9ECcQz)P",
        "role": "admin",
        "telephone_number": "518937947",
    },
    {
        "children": [{"age": 5, "name": "Alan"}],
        "created_at": datetime.datetime(2023, 10, 10, 21, 3, 45),
        "email": "kyle463@example.org",
        "firstname": "Tiffany",
        "password": "ywq%6FzI_o",
        "role": "user",
        "telephone_number": "804241616",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 8, 27, 16, 39, 4),
        "email": "rubengriffin@example.com",
        "firstname": "Cathy",
        "password": "Dw2Bf(Dd!q",
        "role": "user",
        "telephone_number": "594885352",
    },
    {
        "children": [{"age": 8, "name": "Sara"}],
        "created_at": datetime.datetime(2023, 3, 5, 4, 14, 24),
        "email": "brenda74@example.org",
        "firstname": "Amy",
        "password": "+vJCXfFLe0",
        "role": "admin",
        "telephone_number": "361568741",
    },
    {
        "children": [{"age": 15, "name": "Justin"}, {"age": 10, "name": "Sarah"}],
        "created_at": datetime.datetime(2023, 11, 19, 20, 42, 33),
        "email": "kimberlymartin@example.org",
        "firstname": "Michael",
        "password": "ns6REVen+g",
        "role": "admin",
        "telephone_number": "667574950",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 4, 13, 4, 43, 54),
        "email": "john60@example.net",
        "firstname": "Betty",
        "password": "#_ILaeXdj0",
        "role": "admin",
        "telephone_number": "762084369",
    },
    {
        "children": [{"age": 4, "name": "David"}],
        "created_at": datetime.datetime(2023, 6, 24, 13, 48, 25),
        "email": "kcabrera@example.net",
        "firstname": "Blake",
        "password": "gk2VM$qk@S",
        "role": "user",
        "telephone_number": "203818382",
    },
    {
        "children": [{"age": 17, "name": "Michael"}, {"age": 14, "name": "Angela"}],
        "created_at": datetime.datetime(2022, 12, 3, 10, 9, 14),
        "email": "ngreen@example.org",
        "firstname": "Michael",
        "password": "n(9vNQ$jqO",
        "role": "user",
        "telephone_number": "736121560",
    },
    {
        "children": [
            {"age": 17, "name": "Marie"},
            {"age": 8, "name": "George"},
            {"age": 11, "name": "Susan"},
        ],
        "created_at": datetime.datetime(2023, 7, 20, 11, 53, 7),
        "email": "velazquezsierra@example.org",
        "firstname": "Amanda",
        "password": "F9Jf!Bs6_d",
        "role": "admin",
        "telephone_number": "208579481",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 9, 17, 22, 53, 26),
        "email": "acamacho@example.com",
        "firstname": "Travis",
        "password": "_9#hlJNZcV",
        "role": "user",
        "telephone_number": "905910845",
    },
    {
        "children": [{"age": 9, "name": "Jackie"}, {"age": 6, "name": "Mitchell"}],
        "created_at": datetime.datetime(2023, 11, 6, 2, 10, 33),
        "email": "ngutierrez@example.net",
        "firstname": "Donna",
        "password": "@9TcRo15As",
        "role": "user",
        "telephone_number": "504140673",
    },
    {
        "children": [{"age": 12, "name": "Dorothy"}, {"age": 2, "name": "Kristen"}],
        "created_at": datetime.datetime(2023, 6, 2, 11, 12, 5),
        "email": "joshua75@example.org",
        "firstname": "Sandy",
        "password": "&T)u+DAa31",
        "role": "admin",
        "telephone_number": "577969415",
    },
    {
        "children": [
            {"age": 2, "name": "Kimberly"},
            {"age": 4, "name": "Sarah"},
            {"age": 3, "name": "David"},
        ],
        "created_at": datetime.datetime(2023, 6, 9, 7, 47, 58),
        "email": "silvaarthur@example.com",
        "firstname": "Danny",
        "password": "9q(6KpMuvS",
        "role": "admin",
        "telephone_number": "342559287",
    },
    {
        "children": [{"age": 8, "name": "Michael"}, {"age": 9, "name": "Michelle"}],
        "created_at": datetime.datetime(2023, 3, 7, 13, 18, 28),
        "email": "daniel61@example.com",
        "firstname": "Sarah",
        "password": "WAq7M2xG&K",
        "role": "user",
        "telephone_number": "401629185",
    },
    {
        "children": [{"age": 11, "name": "Leonard"}],
        "created_at": datetime.datetime(2022, 12, 12, 15, 42, 28),
        "email": "lisawood@example.org",
        "firstname": "Caroline",
        "password": "&_(8(EJ^j1",
        "role": "user",
        "telephone_number": "617796987",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 10, 23, 16, 46, 46),
        "email": "jboyd@example.org",
        "firstname": "Patricia",
        "password": "_9tGfwed#7",
        "role": "admin",
        "telephone_number": "410836947",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 5, 16, 19, 21, 33),
        "email": "kristen69@example.net",
        "firstname": "Alisha",
        "password": "%Sj6pSOl9s",
        "role": "admin",
        "telephone_number": "701944195",
    },
    {
        "children": [{"age": 11, "name": "Crystal"}, {"age": 12, "name": "Robert"}],
        "created_at": datetime.datetime(2022, 12, 29, 14, 11, 20),
        "email": "stewartpaige@example.org",
        "firstname": "Molly",
        "password": "!DWe5E*kn6",
        "role": "user",
        "telephone_number": "838059352",
    },
    {
        "children": [
            {"age": 7, "name": "Jesse"},
            {"age": 10, "name": "Victor"},
            {"age": 13, "name": "Jonathan"},
        ],
        "created_at": datetime.datetime(2023, 4, 21, 5, 53, 16),
        "email": "victoriataylor@example.net",
        "firstname": "Jamie",
        "password": "+Wu@Pu)y(0",
        "role": "user",
        "telephone_number": "608442660",
    },
    {
        "children": [{"age": 16, "name": "Catherine"}, {"age": 5, "name": "Laurie"}],
        "created_at": datetime.datetime(2023, 5, 31, 12, 36, 7),
        "email": "destinymatthews@example.com",
        "firstname": "Peter",
        "password": "*rFJC0Au@8",
        "role": "user",
        "telephone_number": "367763447",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 8, 27, 14, 57, 51),
        "email": "yconley@example.com",
        "firstname": "Timothy",
        "password": "r^QBH^4n+9",
        "role": "user",
        "telephone_number": "553704593",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 5, 7, 8, 12, 39),
        "email": "pvelazquez@example.org",
        "firstname": "Connie",
        "password": "AVW*9Z)i4u",
        "role": "user",
        "telephone_number": "690145953",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 6, 6, 2, 32, 5),
        "email": "cory34@example.com",
        "firstname": "Michael",
        "password": "!2VLgpDXS6",
        "role": "user",
        "telephone_number": "277615047",
    },
    {
        "children": [{"age": 3, "name": "Dustin"}],
        "created_at": datetime.datetime(2023, 8, 2, 5, 10, 5),
        "email": "gharrington@example.net",
        "firstname": "Curtis",
        "password": "q^oA7P$i+8",
        "role": "admin",
        "telephone_number": "816163817",
    },
    {
        "children": [
            {"age": 12, "name": "Jose"},
            {"age": 2, "name": "Scott"},
            {"age": 16, "name": "Olivia"},
        ],
        "created_at": datetime.datetime(2023, 7, 11, 17, 16, 44),
        "email": "kgreer@example.com",
        "firstname": "Angela",
        "password": "7GRZImGp!t",
        "role": "admin",
        "telephone_number": "216474381",
    },
    {
        "children": [{"age": 16, "name": "Belinda"}],
        "created_at": datetime.datetime(2023, 9, 30, 5, 34, 42),
        "email": "luisjohnson@example.org",
        "firstname": "Ashley",
        "password": "@A60KjMx7t",
        "role": "user",
        "telephone_number": "124252062",
    },
    {
        "children": [{"age": 1, "name": "Victoria"}],
        "created_at": datetime.datetime(2023, 7, 28, 18, 13, 7),
        "email": "hoffmanlisa@example.net",
        "firstname": "Brian",
        "password": "&Ys8nbMmUM",
        "role": "user",
        "telephone_number": "174746366",
    },
    {
        "children": [{"age": 17, "name": "Margaret"}, {"age": 17, "name": "Gregory"}],
        "created_at": datetime.datetime(2023, 8, 25, 22, 15, 1),
        "email": "nicholsamanda@example.net",
        "firstname": "John",
        "password": "Ns83PGcqR_",
        "role": "user",
        "telephone_number": "727231114",
    },
    {
        "children": [
            {"age": 12, "name": "Michael"},
            {"age": 6, "name": "Theresa"},
            {"age": 1, "name": "Judith"},
        ],
        "created_at": datetime.datetime(2023, 8, 23, 23, 27, 9),
        "email": "tamara37@example.com",
        "firstname": "Don",
        "password": "jQ66IIlR*1",
        "role": "user",
        "telephone_number": "612660796",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 8, 11, 23, 17, 16),
        "email": "velasquezkeith@example.org",
        "firstname": "Mark",
        "password": "GW4Ft8zbi&",
        "role": "user",
        "telephone_number": "813868944",
    },
    {
        "children": [
            {"age": 5, "name": "Scott"},
            {"age": 9, "name": "James"},
            {"age": 8, "name": "Zachary"},
        ],
        "created_at": datetime.datetime(2023, 4, 30, 14, 42, 35),
        "email": "alan49@example.com",
        "firstname": "Christopher",
        "password": "f)1)2HvlN7",
        "role": "user",
        "telephone_number": "743328816",
    },
    {
        "children": [{"age": 8, "name": "Eric"}, {"age": 17, "name": "Shelia"}],
        "created_at": datetime.datetime(2023, 6, 7, 4, 3, 48),
        "email": "dennis32@example.net",
        "firstname": "Curtis",
        "password": "_Js5&&AbQ!",
        "role": "user",
        "telephone_number": "107058738",
    },
    {
        "children": [{"age": 17, "name": "Dean"}, {"age": 6, "name": "Brittany"}],
        "created_at": datetime.datetime(2023, 4, 27, 10, 5, 56),
        "email": "tony08@example.net",
        "firstname": "David",
        "password": "(KJiF0yPB6",
        "role": "user",
        "telephone_number": "463078584",
    },
    {
        "children": [
            {"age": 7, "name": "Denise"},
            {"age": 4, "name": "Kyle"},
            {"age": 4, "name": "Roberto"},
        ],
        "created_at": datetime.datetime(2023, 10, 12, 17, 20, 35),
        "email": "jonathan22@example.com",
        "firstname": "Erica",
        "password": "DG8Xok77#6",
        "role": "user",
        "telephone_number": "585173108",
    },
    {
        "children": [{"age": 1, "name": "Jonathan"}, {"age": 11, "name": "Natalie"}],
        "created_at": datetime.datetime(2022, 12, 5, 4, 34, 20),
        "email": "matthewdecker2@example.com",
        "firstname": "Madeline",
        "password": "2p$v9zPt1+",
        "role": "user",
        "telephone_number": "441935720",
    },
    {
        "children": [{"age": 3, "name": "Deanna"}],
        "created_at": datetime.datetime(2023, 5, 30, 4, 45, 20),
        "email": "riggsbruce3@example.org",
        "firstname": "Ebony",
        "password": "@5j%ih7y!R",
        "role": "user",
        "telephone_number": "289862947",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 5, 30, 4, 1, 59),
        "email": "erica90@example.net",
        "firstname": "James",
        "password": "8UZLqatV%8",
        "role": "admin",
        "telephone_number": "784578915",
    },
    {
        "children": [{"age": 9, "name": "Robert"}],
        "created_at": datetime.datetime(2023, 3, 1, 15, 40, 39),
        "email": "levi49@example.org",
        "firstname": "Sandra",
        "password": ")*0v4YCgU!",
        "role": "user",
        "telephone_number": "267687714",
    },
    {
        "children": [
            {"age": 1, "name": "Mary"},
            {"age": 15, "name": "Mary"},
            {"age": 2, "name": "Evan"},
        ],
        "created_at": datetime.datetime(2023, 4, 1, 23, 40, 5),
        "email": "zeverett@example.org",
        "firstname": "Eric",
        "password": "n@8AymNdC*",
        "role": "admin",
        "telephone_number": "110355347",
    },
    {
        "children": [{"age": 14, "name": "Kristin"}],
        "created_at": datetime.datetime(2023, 2, 11, 14, 29, 37),
        "email": "greenmadison@example.net",
        "firstname": "Kevin",
        "password": "&S1XUo94)k",
        "role": "admin",
        "telephone_number": "227397825",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 1, 2, 0, 48, 15),
        "email": "litiffany@example.org",
        "firstname": "Tyler",
        "password": "!Y2m4%ysM4",
        "role": "user",
        "telephone_number": "795776161",
    },
    {
        "children": [{"age": 18, "name": "Anna"}, {"age": 11, "name": "Mindy"}],
        "created_at": datetime.datetime(2023, 8, 27, 23, 36),
        "email": "lowerykimberly@example.net",
        "firstname": "Tanner",
        "password": "6mKY!nP^+y",
        "role": "admin",
        "telephone_number": "604020303",
    },
    {
        "children": [
            {"age": 2, "name": "John"},
            {"age": 16, "name": "Christopher"},
            {"age": 17, "name": "Courtney"},
        ],
        "created_at": datetime.datetime(2023, 5, 11, 19, 29, 50),
        "email": "johnscourtney@example.com",
        "firstname": "Brenda",
        "password": "S_d0SUo&Ce",
        "role": "admin",
        "telephone_number": "859092651",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 6, 15, 2, 30, 15),
        "email": "christopher52@example.com",
        "firstname": "Sarah",
        "password": "@0iZyh6uIY",
        "role": "admin",
        "telephone_number": "831311035",
    },
    {
        "children": [{"age": 16, "name": "Phillip"}],
        "created_at": datetime.datetime(2023, 7, 2, 23, 12, 58),
        "email": "norrissabrina@example.org",
        "firstname": "Jeffrey",
        "password": "_9fM7zav#B",
        "role": "admin",
        "telephone_number": "987093912",
    },
    {
        "children": [
            {"age": 7, "name": "Karen"},
            {"age": 11, "name": "Danielle"},
            {"age": 7, "name": "Dustin"},
        ],
        "created_at": datetime.datetime(2023, 1, 20, 8, 50, 11),
        "email": "trobbins@example.net",
        "firstname": "Joan",
        "password": "@%xHuZl)9l",
        "role": "admin",
        "telephone_number": "232756993",
    },
    {
        "children": [{"age": 13, "name": "Dustin"}],
        "created_at": datetime.datetime(2023, 7, 7, 18, 2, 34),
        "email": "faulknersusan@example.net",
        "firstname": "Caroline",
        "password": "L(1RUoaJDH",
        "role": "user",
        "telephone_number": "217311726",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 11, 20, 7, 22, 51),
        "email": "carterlindsey@example.org",
        "firstname": "Kathryn",
        "password": "+sUVpIkkY6",
        "role": "user",
        "telephone_number": "108835339",
    },
    {
        "children": [
            {"age": 17, "name": "Diana"},
            {"age": 8, "name": "April"},
            {"age": 17, "name": "James"},
        ],
        "created_at": datetime.datetime(2023, 10, 20, 3, 16, 47),
        "email": "ronald99@example.com",
        "firstname": "Chad",
        "password": "Q3XWW+Uc*Z",
        "role": "user",
        "telephone_number": "882294581",
    },
    {
        "children": [{"age": 10, "name": "Dan"}],
        "created_at": datetime.datetime(2023, 8, 31, 10, 12, 45),
        "email": "gregory80@example.com",
        "firstname": "Sean",
        "password": "sXs!4Mzjx%",
        "role": "user",
        "telephone_number": "650232530",
    },
    {
        "children": [{"age": 6, "name": "Samantha"}],
        "created_at": datetime.datetime(2023, 11, 8, 16, 38, 28),
        "email": "michelle93@example.org",
        "firstname": "George",
        "password": "+hL*hdte2H",
        "role": "admin",
        "telephone_number": "681988567",
    },
    {
        "children": [{"age": 4, "name": "Teresa"}],
        "created_at": datetime.datetime(2022, 12, 4, 8, 30, 37),
        "email": "andrew36@example.net",
        "firstname": "Brandy",
        "password": "(UVIl#9&q7",
        "role": "admin",
        "telephone_number": "686983157",
    },
    {
        "children": [{"age": 2, "name": "Christopher"}],
        "created_at": datetime.datetime(2023, 8, 25, 1, 39, 6),
        "email": "tammy87@example.com",
        "firstname": "Jeff",
        "password": "cjZ6Z%pB+_",
        "role": "user",
        "telephone_number": "920237730",
    },
    {
        "children": [{"age": 12, "name": "Jamie"}],
        "created_at": datetime.datetime(2023, 5, 2, 16, 57, 13),
        "email": "cameronguzman@example.com",
        "firstname": "Timothy",
        "password": "&1WU31#v$o",
        "role": "admin",
        "telephone_number": "279179128",
    },
    {
        "children": [{"age": 2, "name": "Jennifer"}, {"age": 10, "name": "Omar"}],
        "created_at": datetime.datetime(2023, 7, 19, 0, 22, 43),
        "email": "alicia41@example.com",
        "firstname": "Felicia",
        "password": "^rf3mkTt&)",
        "role": "user",
        "telephone_number": "394426853",
    },
    {
        "children": [
            {"age": 15, "name": "Mark"},
            {"age": 2, "name": "Kimberly"},
            {"age": 1, "name": "Paul"},
        ],
        "created_at": datetime.datetime(2023, 3, 6, 15, 46, 8),
        "email": "jason92@example.org",
        "firstname": "Donna",
        "password": "Z#7VMvf%d^",
        "role": "user",
        "telephone_number": "893849179",
    },
    {
        "children": [
            {"age": 15, "name": "Christopher"},
            {"age": 8, "name": "Lisa"},
            {"age": 1, "name": "Brenda"},
        ],
        "created_at": datetime.datetime(2023, 10, 24, 18, 32, 20),
        "email": "johnsongabrielle@example.com",
        "firstname": "Amanda",
        "password": "R)c1JJtz!&",
        "role": "admin",
        "telephone_number": "698312978",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 6, 30, 10, 22, 59),
        "email": "biancataylor@example.net",
        "firstname": "Mark",
        "password": "6cUYasjf^4",
        "role": "user",
        "telephone_number": "847940862",
    },
    {
        "children": [
            {"age": 12, "name": "Rachel"},
            {"age": 7, "name": "Jennifer"},
            {"age": 18, "name": "Jermaine"},
        ],
        "created_at": datetime.datetime(2022, 12, 15, 5, 29, 5),
        "email": "mooremorgan@example.net",
        "firstname": "Logan",
        "password": "4bgDfF4t*^",
        "role": "admin",
        "telephone_number": "716290783",
    },
    {
        "children": [],
        "created_at": datetime.datetime(2023, 11, 13, 14, 10, 9),
        "email": "lisa93@example.com",
        "firstname": "Joseph",
        "password": "!q62J8^sYb",
        "role": "user",
        "telephone_number": "756037486",
    },
    {
        "children": [
            {"age": 12, "name": "Steven"},
            {"age": 18, "name": "Christine"},
            {"age": 6, "name": "Rachel"},
        ],
        "created_at": datetime.datetime(2023, 4, 12, 22, 7, 59),
        "email": "hunter96@example.org",
        "firstname": "Shannon",
        "password": "sD3NddkqB*",
        "role": "admin",
        "telephone_number": "121975731",
    },
    {
        "children": [
            {"age": 14, "name": "Jessica"},
            {"age": 11, "name": "Megan"},
            {"age": 9, "name": "Michael"},
        ],
        "created_at": datetime.datetime(2023, 11, 10, 9, 52, 49),
        "email": "weisskristina@example.net",
        "firstname": "Steven",
        "password": "9T1zNeAN(2",
        "role": "user",
        "telephone_number": "691250247",
    },
    {
        "children": [
            {"age": 1, "name": "Tracy"},
            {"age": 1, "name": "Joseph"},
            {"age": 8, "name": "Whitney"},
        ],
        "created_at": datetime.datetime(2023, 1, 18, 20, 39, 19),
        "email": "ashleyschwartz@example.org",
        "firstname": "Mark",
        "password": "I35_C9id^P",
        "role": "admin",
        "telephone_number": "967426092",
    },
    {
        "children": [{"age": 4, "name": "Sheila"}, {"age": 12, "name": "Laurie"}],
        "created_at": datetime.datetime(2023, 4, 28, 11, 35, 28),
        "email": "halemisty@example.net",
        "firstname": "Brianna",
        "password": "_r1CEmbZHe",
        "role": "admin",
        "telephone_number": "505400027",
    },
    {
        "children": [{"age": 15, "name": "John"}, {"age": 13, "name": "Brian"}],
        "created_at": datetime.datetime(2023, 4, 5, 3, 50, 42),
        "email": "erik91@example.org",
        "firstname": "Jeffrey",
        "password": "25pEhHfx$Y",
        "role": "user",
        "telephone_number": "854869516",
    },
]
