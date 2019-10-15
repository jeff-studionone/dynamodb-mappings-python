
## Introduction
This is a python recursion that will allow you to conver your dictionary values into the correct structure necessary to save the data in DynamoDB.

## Use

### Mapping
You just need to send to the function `build_from_model(data)` and pass your dictionary that will return a dictionary with the data structure that you need.

### Mapping back
You just need to send to the function `get_from_model(data)` and pass your dictionary that will return a dictionary with the data structure that you need.

#### Note:
Be careful because `build_from_model` return `{'M': your-data}` and `get_from_model` requires a dictionary with `{'M': your-data}`


```python
response = client.put_item(
    TableName='string',
    Item={
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    Expected={
        'string': {
            'Value': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            },
            'Exists': True|False,
            'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH',
            'AttributeValueList': [
                {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
            ]
        }
    },
    ReturnValues='NONE'|'ALL_OLD'|'UPDATED_OLD'|'ALL_NEW'|'UPDATED_NEW',
    ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
    ReturnItemCollectionMetrics='SIZE'|'NONE',
    ConditionalOperator='AND'|'OR',
    ConditionExpression='string',
    ExpressionAttributeNames={
        'string': 'string'
    },
    ExpressionAttributeValues={
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    }
)

```
