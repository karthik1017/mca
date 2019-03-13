

db.createCollection("invoice");

db.invoice.insertMany(
    [
        {
           id:1,
           item:"dairy milk",
           qty:100,
           rate:10,
           date_of_invoice:new Date("2014-12-05")
        },
        {
            id:2,
            item:"milky bar",
            qty:1000,
            rate:15,
            date_of_invoice:new Date("2014-10-02")
         },
         {
            id:3,
            item:"polo",
            qty:50,
            rate:5,
            date_of_invoice:new Date("2016-12-04")
         },
         {
            id:4,
            item:"popins",
            qty:500,
            rate:10,
            date_of_invoice:new Date("2018-12-23")
         },
         {
            id:5,
            item:"coffee bites",
            qty:75,
            rate:1,
            date_of_invoice:new Date("2015-07-04")
         },
         {
            id:6,
            item:"mango bites",
            qty:400,
            rate:1,
            date_of_invoice:new Date("2016-1-10")
         },
         {
            id:7,
            item:"kaccha mango bites",
            qty:300,
            rate:1,
            date_of_invoice:new Date("2017-2-05")
         },
         {
            id:8,
            item:"pata pat",
            qty:50,
            rate:0.5,
            date_of_invoice:new Date("2018-12-05")
         },
         {
            id:9,
            item:"krackers",
            qty:300,
            rate:5,
            date_of_invoice:new Date("2015-06-05")
         },
         {
            id:10,
            item:"cola mint",
            qty:500,
            rate:10,
            date_of_invoice:new Date("2017-10-03")
         },
    ]
)

db.invoice.insertMany([{
    id:11,
    item:"pepsi mint",
    qty: 100,
    rate:10,
    date_of_invoice:new Date("2017-10-03")
},{
    id:12,
    item:"fanta mint",
    qty: 300,
    rate:10,
    date_of_invoice:new Date("2017-10-03")
}])

db.invoice.aggregate(
    [
       {
         $group : {
            _id : { month: { $month: "$date_of_invoice" }, day: { $dayOfMonth: "$date_of_invoice" }, year: { $year: "$date_of_invoice" } },
            totalPrice: { $sum: { $multiply: [ "$rate", "$qty" ] } },
            averageQuantity: { $avg: "$qty" },
            count: { $sum: 1 }
         }
       }
    ]
).pretty()


db.invoice.aggregate(
    [
       {
         $group : {
            _id : { month: { $month: "$date_of_invoice" }, day: { $dayOfMonth: "$date_of_invoice" }, year: { $year: "$date_of_invoice" } },
            totalPrice: { $sum: { $multiply: [ "$rate", "$qty" ] } },
            averageQuantity: { $avg: "$qty" },
            count: { $sum: 1 }
         }
       }
    ]
).pretty()

db.invoice.aggregate(
    [
       {
        $match : {date_of_invoice : "2014-12-05"}
       },
       {
         $group : {
            _id : { month: { $month: "$date_of_invoice" }, day: { $dayOfMonth: "$date_of_invoice" }, year: { $year: "$date_of_invoice" },item :"$item"},
            totalPrice: { $sum: { $multiply: [ "$rate", "$qty" ] } },
            averageQuantity: { $avg: "$qty" },
            count: { $sum: 1 }
         }
       }
    ]
).pretty()


db.invoice.aggregate( [ { $group : { _id : "$item" } } ] ).pretty();

db.invoice.aggregate(
    [
      { $group : { _id : "$item", invoiceDate: { $push: "$date_of_invoice" } } }
    ]
 ).pretty();

db.invoice.find().skip(3).limit(5).pretty()


// scenario 2

// 1)

db.createCollection("employees")

// 2)

db.employees.insertMany(
    [
        {
            "id":1,
            "emp_code":"EMP-001",
            "emp_name":"KARTHIK",
            "doj":new Date("2018-12-23"),
            "salary":10000
        },
        {
            "id":2,
            "emp_code":"EMP-002",
            "emp_name":"HARSHA",
            "doj":new Date("2018-2-20"),
            "salary":20000
        },
        {
            "id":3,
            "emp_code":"EMP-003",
            "emp_name":"JEEVAN",
            "doj":new Date("2017-1-23"),
            "salary":30000
        },
        {
            "id":4,
            "emp_code":"EMP-004",
            "emp_name":"LAKSHMAN",
            "doj":new Date("2016-12-23"),
            "salary":30000
        },
        {
            "id":5,
            "emp_code":"EMP-005",
            "emp_name":"RAMA",
            "doj":new Date("2014-12-02"),
            "salary":40000
        },
        {
            "id":6,
            "emp_code":"EMP-006",
            "emp_name":"KRISHNA",
            "doj":new Date("2015-10-23"),
            "salary":90000
        },
        {
            "id":7,
            "emp_code":"EMP-007",
            "emp_name":"SITA",
            "doj":new Date("2015-02-03"),
            "salary":40000
        },
        {
            "id":8,
            "emp_code":"EMP-008",
            "emp_name":"VEDHANTH",
            "doj":new Date("2013-10-23"),
            "salary":90000
        },
        {
            "id":9,
            "emp_code":"EMP-009",
            "emp_name":"VYASA",
            "doj":new Date("2012-05-21"),
            "salary":60000
        },
        {
            "id":10,
            "emp_code":"EMP-010",
            "emp_name":"VAIDEHI",
            "doj":"2016-12-23",
            "salary":70000
        },
    ]
)

// 3)

db.employees.aggregate([{$project:{emp_code:1,emp_name:1,}}]).pretty()


// 4) 

db.employee.updateOne({id: 10}, {
    $set: {
      deduction: {
        pf: 4000,
        pt: 3000,
        it: 200
      }
    }
  })
