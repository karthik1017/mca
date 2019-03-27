//2
db.createCollection("restaurants");

//3
db.restaurants.insertMany(
    [
        {
            id:1,
            name:"the bell hotel",
            cusine:"continentel",
            address:{
                building:102,
                city:"bengaluru",
                pincode:"560073"
            },
            star:3,
            locality:"jayanagar",
            grade:[
                {
                    date:new Date("2019-3-4"),
                    grade:"A",
                    score:8
                },
                {
                    data:new Date("2014-3-5"),
                    grade:"B",
                    score:7
                }
            ]
        },
        {
            id:2,
            name:"the empire hotel",
            cusine:"mughal",
            address:{
                building:1002,
                city:"bengaluru",
                pincode:"560023"
            },
            star:3,
            locality:"koramangala",
            grade:[
                {
                    date:new Date("2018-5-23"),
                    grade:"A",
                    score:9
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"B",
                    score:7
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"c",
                    score:4
                },
            ]
        },
        {
            id:3,
            name:"the shivaji military hotel",
            cusine:"Marati",
            address:{
                building:202,
                city:"bengaluru",
                pincode:"560072"
            },
            star:3,
            locality:"banashankari",
            grade:[
                {
                    date:new Date("2017-3-4"),
                    grade:"A",
                    score:10
                },
                {
                    data:new Date("2019-3-5"),
                    grade:"A",
                    score:10
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"B",
                    score:8
                }
            ]
        },
        {
            id:4,
            name:"the udupi grand",
            cusine:"south indian",
            address:{
                building:7900,
                city:"bengaluru",
                pincode:"560043"
            },
            star:3,
            locality:"RR nagar",
            grade:[
                {
                    date:new Date("2019-3-4"),
                    grade:"A",
                    score:8
                },
                {
                    data:new Date("2014-3-5"),
                    grade:"B",
                    score:7
                }
            ]
        },
        {
            id:5,
            name:"the biryani paradise",
            cusine:"andhra cusine",
            address:{
                building:702,
                city:"bengaluru",
                pincode:"560053"
            },
            star:5,
            locality:"jayanagar",
            grade:[
                {
                    date:new Date("2019-3-4"),
                    grade:"A",
                    score:8
                },
                {
                    data:new Date("2014-3-5"),
                    grade:"B",
                    score:7
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"B",
                    score:7
                }
            ]
        },
        {
            id:6,
            name:"kebab magic",
            cusine:"mughal",
            address:{
                building:6602,
                city:"bengaluru",
                pincode:"560063"
            },
            star:5,
            locality:"RR nagar  ",
            grade:[
                {
                    date:new Date("2017-3-4"),
                    grade:"c",
                    score:5
                },
                {
                    data:new Date("2014-3-5"),
                    grade:"A",
                    score:9
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"B",
                    score:7
                }
            ]
        },
        {
            id:7,
            name:"A2B",
            cusine:"south",
            address:{
                building:2102,
                city:"bengaluru",
                pincode:"560043"
            },
            star:3,
            locality:"jayanagar",
            grade:[
                {
                    date:new Date("2019-3-4"),
                    grade:"A",
                    score:8
                },
                {
                    data:new Date("2014-3-5"),
                    grade:"B",
                    score:7
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"B",
                    score:7
                }
            ]
        },
        {
            id:8,
            name:"the ITC",
            cusine:"continental",
            address:{
                building:1102,
                city:"bengaluru",
                pincode:"560083"
            },
            star:7,
            locality:"MG road",
            grade:[
                {
                    date:new Date("2019-3-4"),
                    grade:"A",
                    score:8
                },
                {
                    data:new Date("2014-3-5"),
                    grade:"A",
                    score:10
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"B",
                    score:7
                }
            ]
        },
        {
            id:9,
            name:"vidyarthi bhavan",
            cusine:"south",
            address:{
                building:4102,
                city:"bengaluru",
                pincode:"560093"
            },
            star:3,
            locality:"basavanagudi",
            grade:[
                {
                    date:new Date("2019-3-4"),
                    grade:"A",
                    score:9
                },
                {
                    data:new Date("2014-3-5"),
                    grade:"A",
                    score:10
                },
                {
                    data:new Date("2019-6-12"),
                    grade:"A",
                    score:9
                },
                {
                    id:10,
                    name:"CTR",
                    cusine:"south",
                    address:{
                        building:412,
                        city:"bengaluru",
                        pincode:"560193"
                    },
                    star:3,
                    locality:"malleshwaram",
                    grade:[
                        {
                            date:new Date("2019-3-4"),
                            grade:"A",
                            score:9
                        },
                        {
                            data:new Date("2018-2-11"),
                            grade:"A",
                            score:9
                        },
                        {
                            data:new Date("2019-6-12"),
                            grade:"A",
                            score:9
                        }
                    ]
                }
            ]
        },
    ]
)

//4)
db.restaurants.find().pretty();

//5)
db.restaurants.find({},{id:1,name:1,cuisine:1}).pretty();

//6)
db.restaurants.find({locality:"RR nagar"}).limit(5).pretty();

//7)
db.restaurants.find(
    {"grade.score" :
       {$mod : [7,0]}
    },
       {"id" : 1,"name":1,"grade":1}
).pretty();

//8)
db.restaurants.find().sort(
    {"cuisine":1,"locality" : -1}
).pretty();

//9
db.restaurants.find( 
    { "grade.1.date": ISODate("2018-02-11T00:00:00Z"), 
      "grade.1.grade":"A" , 
      "grade.1.score" :9
    }, 
     {"id" : 1,"name":1,"grade":1}
 ).pretty();

 //10
 db.restaurants.find().sort(
     {"name":1}
 ).pretty();

 //14
 db.restaurants.find({ grade : { $elemMatch: {"grade.score": { $gt : 90 }}}});

 //15
 db.restaurants.find(
	{
		$and:
			[
				{"cusine" : {$ne :"mughal"}},
				{"grade.score" : {$gt : 7}}
			]
	}
).pretty()

//16
db.restaurants.find( {
	"cusine" : {$ne : "mughal"},
	"grade.grade" :"A",
	"locality": {$ne : "Jaynagar"}
} 
).sort({ "cuisine":-1 }).pretty()

//17
db.restaurants.find(
	{ name: /uth$/ },
	{
		id : 1,
		name: 1,
		locality: 1,
		cusine: 1
	}
).pretty()

//18
db.restaurants.find(
	{ 
		"locality": "MG Road", 
		$or: 
		[
			{ "cusine" : "continental" },
			{ "cusine" : "mughal    " }
		] 
	} 
).pretty()
