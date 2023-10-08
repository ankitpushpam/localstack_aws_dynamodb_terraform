import boto3
import json
from decimal import Decimal

# Initialize the DynamoDB resource
def initialize_dynamodb_resource():
    return boto3.resource('dynamodb', endpoint_url='http://localhost:4566', region_name='us-east-1', aws_access_key_id='mock_access_key', aws_secret_access_key='mock_secret_key')

# Upload batch records to the 'order' table
def upload_batch_records_to_order_table(dynamodb_resource):
    order_table_name = 'order'
    order_table = dynamodb_resource.Table(order_table_name)

    orders = [
        {"order_id": "3", "customer_name": "Charlie", "total_amount": Decimal('300.0')},
        {"order_id": "4", "customer_name": "David", "total_amount": Decimal('400.0')},
    ]

    with order_table.batch_writer() as batch:
        for order in orders:
            batch.put_item(Item=order)

# Upload batch records to the 'user' table
def upload_batch_records_to_user_table(dynamodb_resource):
    user_table_name = 'user'
    user_table = dynamodb_resource.Table(user_table_name)

    users = [
        {"user_id": "1", "user_name": "Alice"},
        {"user_id": "2", "user_name": "Bob"},
    ]

    with user_table.batch_writer() as batch:
        for user in users:
            batch.put_item(Item=user)

# Read a single item from the 'order' table
def read_single_item_from_order_table(dynamodb_resource, order_id):
    order_table_name = 'order'
    order_table = dynamodb_resource.Table(order_table_name)

    response = order_table.get_item(Key={"order_id": order_id})
    return response.get("Item")

# Read batch items from the 'user' table
def read_batch_items_from_user_table(dynamodb_resource):
    user_table_name = 'user'
    user_table = dynamodb_resource.Table(user_table_name)

    response = user_table.scan()
    return response.get("Items", [])

# Save data to a JSON file
def save_to_json_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2, default=str)

# Main function
def main():
    dynamodb_resource = initialize_dynamodb_resource()

    upload_batch_records_to_order_table(dynamodb_resource)
    upload_batch_records_to_user_table(dynamodb_resource)  # Upload data to the user table

    order_id = "3"
    order_item = read_single_item_from_order_table(dynamodb_resource, order_id)
    print("Single Order Item:")
    print(order_item)

    user_items = read_batch_items_from_user_table(dynamodb_resource)
    print("Batch User Items:")
    print(user_items)

    save_to_json_file(order_item, "order_item.json")
    save_to_json_file(user_items, "user_items.json")

    print("Records uploaded and saved successfully.")

if __name__ == "__main__":
    main()
