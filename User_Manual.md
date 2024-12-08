# Online Restaurant Ordering System API

**User Manual**

## Overview
The Online Restaurant Ordering System API enables seamless interaction with restaurant menus, order placements, customer reviews, and payment processing. Designed for integration into web and mobile applications, the API provides a robust and user-friendly way to manage restaurant operations and customer engagement.

### Key Features:
- View and manage restaurant menus
- Place and track customer orders
- Handle payments and promotions
- Enable customer feedback and reviews

## Setup Instructions

### Prerequisites:
- Python 3.9+
- A virtual environment tool like `venv` or `virtualenv`
- Dependency management through `pip`
- Access to a database (e.g., PostgreSQL)

### Installation Steps:
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd Final-Project-master
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file with the following:
   ```env
   DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>
   SECRET_KEY=<your_secret_key>
   ```

5. **Run the Server**:
   ```bash
   python api/main.py
   ```
   The server will be accessible at `http://127.0.0.1:8000/`.

## Usage Examples

### Base URL
The base URL for all API endpoints is:
```
http://127.0.0.1:8000/api
```

### Example 1: Fetch Menu Items
**Endpoint**: `/menu_items`

**Request**:
```bash
GET /api/menu_items
```

**Response**:
```json
[
  {
    "id": 1,
    "name": "Margherita Pizza",
    "price": 12.99,
    "description": "Classic cheese pizza with tomato sauce."
  },
  {
    "id": 2,
    "name": "Caesar Salad",
    "price": 8.99,
    "description": "Crisp romaine lettuce with Caesar dressing."
  }
]
```

### Example 2: Place an Order
**Endpoint**: `/orders`

**Request**:
```bash
POST /api/orders
Content-Type: application/json

{
  "customer_id": 1,
  "menu_item_ids": [1, 2],
  "payment_method": "credit_card"
}
```

**Response**:
```json
{
  "order_id": 101,
  "status": "confirmed",
  "total_price": 21.98
}
```

### Example 3: Submit a Review
**Endpoint**: `/reviews`

**Request**:
```bash
POST /api/reviews
Content-Type: application/json

{
  "customer_id": 1,
  "menu_item_id": 1,
  "rating": 5,
  "comment": "Delicious pizza!"
}
```

**Response**:
```json
{
  "review_id": 301,
  "status": "submitted"
}
```
