# Flask User List Manager

This is a simple Flask web application that manages a list of users through basic `POST` operations such as adding, removing, or checking the existence of a user in the list.

## Features

- **Add a user**: Add a new user to the list.
- **Remove a user**: Remove a user from the list.
- **Check if a user exists**: Verify if a user is present in the list.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML (rendered by Flask)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask (can be installed via `pip`)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/flask-user-list-manager.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd flask-user-list-manager
    ```

3. **Install dependencies**:

    Make sure Flask is installed:

    ```bash
    pip install Flask
    ```

4. **Run the application**:

    ```bash
    python app.py
    ```

5. Open your browser and go to:

    ```
    http://127.0.0.1:5000
    ```

## Endpoints

### 1. `GET /`

Renders the homepage (`index.html`).

### 2. `POST /alterlist`

This endpoint accepts a `POST` request to modify the user list.

- **Request Body** (JSON):
  ```json
  {
      "number": "123",       // The user number to add, remove, or check
      "option": "add"        // Action to perform: "add", "remove", or "exist"
  }

