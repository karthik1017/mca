

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


