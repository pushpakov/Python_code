#### write queries for following ques:

## Aggregation:

# How can I group documents in a collection based on a specific field and calculate the sum of another field for each group?
-->> Assuming the document contains the field like :
                       db.students.insertMany([
                                                { name : "pushpak",salary : 1000000, month : 2},
                                                { name : "kumar",salary : 134000, month : 7},
                                            ]);

    Then based on specific field the document can be collected with the sum of another field for each group as like here we are providing the totalSalary earned by the employee including all the month :

        db.documents.aggregate([
                                {
                                    $group: {
                                                name: "$name", 
                                                totalAmount: { $sum: { $multiply: ["$salary", "$month"] } } 
                                            }
                                }
                                ])

        --> RESULT :- { "_id" : "pushpak", "totalAmount" : 2000000 }
                      { "_id" : "kumar", "totalAmount" : 938000 }


# How can I join two collections in MongoDB using the $lookup aggregation stage?
-->> To join the two collection in Mongodb we will first create or take two collection and then will join the one inside other collection    which will be collected inside an array 
for example :- 

        `
        <!-- order collection -->
                                db.orders.insertMany([
                                {id:1, item_name : "bat", price : 15000, quantity : 2},
                                { id:2, item_name : "ball", price : 1700, quantity : 7},
                                ]);

        <!-- customer collection -->
                                db.customers.insertMany([
                                {order_id:2, name : "pushpak",address : "bokaro", state : "jharkhand"},
                                { order_id:1, name : "kumar",address : "hyderabad", state : "telangana"},
                                ]);
                        
        <!-- aggregation operation to join customer collection inside order collection -->
                                db.orders.aggregate([
                                                        {
                                                            $lookup: {
                                                                        from: "customers",
                                                                        localField: "id",
                                                                        foreignField: "order_id",
                                                                        as: "customerInfo"
                                                                    }
                                                        }
                                                    ])
        <!-- RESULT  -->
                                { "_id" : ObjectId("642d3031e4b1c016df8bc11a"), "id" : 1, "item_name" : "bat", "price" : 15000, "quantity" : 2, "customerInfo" : [ { "_id" : ObjectId("642d3031e4b1c016df8bc11d"), "order_id" : 1, "name" : "kumar", "address" : "hyderabad", "state" : "telangana" } ] }

                                { "_id" : ObjectId("642d3031e4b1c016df8bc11b"), "id" : 2, "item_name" : "ball", "price" : 1700, "quantity" : 7, "customerInfo" : [ { "_id" : ObjectId("642d3031e4b1c016df8bc11c"), "order_id" : 2, "name" : "pushpak", "address" : "bokaro", "state" : "jharkhand" } ] }
        `

# How can I use the $bucket aggregation stage to group documents into ranges based on a specific field?
-->> To use $bucket aggregatioon stage to group documents into ranges based on a specific field :

                `
                    <!-- order collection -->
                            db.orders.insertMany([
                                                    {id:1, item_name : "bat", price : 15000, quantity : 2},
                                                    { id:2, item_name : "ball", price : 1700, quantity : 7},
                                                    { id:3, item_name : "gloves", price : 800, quantity : 9},
                                                    { id:3, item_name : "pad", price : 2500, quantity : 71},
                                                    { id:4, item_name : "knee_guard", price : 450, quantity : 57},
                                                    { id:5, item_name : "helmet", price : 1700, quantity : 78},
                                                    { id:6, item_name : "stumps", price : 1100, quantity : 77},
                                                    { id:7, item_name : "shorts", price : 300, quantity : 877},
                                                ]);

                    <!-- aggregation operation  -->
                            db.orders.aggregate([ 
                                                    {
                                                        $bucket: {
                                                        groupBy: "$price",
                                                        boundaries: [0, 500, 1000, 1500, 2500, 3500],
                                                        default: "Unknown",
                                                        output: {
                                                            "count_varity_type": { $sum: 1 }
                                                        }
                                                        }
                                                    }
                                                ])

                    <!-- RESULT -->
                                                { "_id" : 0, "count_varity_type" : 2 }
                                                { "_id" : 500, "count_varity_type" : 1 }
                                                { "_id" : 1000, "count_varity_type" : 1 }
                                                { "_id" : 1500, "count_varity_type" : 2 }
                                                { "_id" : 2500, "count_varity_type" : 1 }
                                                { "_id" : "Unknown", "count_varity_type" : 1 }
                `

## Filter:
    How can I query a collection to return all documents that contain a specific field?
    How can I filter documents based on multiple criteria using the $and operator?
    How can I query a collection to return all documents that have a specific field value within an array?
# Update:
    How can I update a single document in a collection based on its ID?
    How can I update multiple documents in a collection based on a specific field value using the $set operator?
    How can I use the $inc operator to increment a specific field value in all documents that match a certain criteria?



