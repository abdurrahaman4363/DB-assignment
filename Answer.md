### Answer

### 1.Question
#### Explain the relationship between the "Product" and "Product_Category" entities from the above diagram ?

#### Answer:
The relationship between the "Product" and "Product_Category" entities is like a parent-child relationship. Just like how a parent can have multiple children but each child has only one parent, one category can have multiple products (children), but each product belongs to only one category (parent)." The relationship is established through the "category_id" column in the "Product" table, which references the primary key "id" column in the "Product_Category" table.

### 2.Question
#### How could you ensure that each product in the "Product" table has a valid category assigned to it ?

#### Answer:
To ensure that every product in the "Product" table has a proper category assigned, we implement a system using foreign key constraints. This ensures that the "category_id" column in the "Product" table always matches a valid category ID from the "Product_Category" table. In other words, each product's category ID must exist in our category list before it's allowed in the product table. This helps us maintain accurate and consistent data, preventing the addition of products with invalid category IDs.
