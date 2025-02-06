# Sympla Events Explorer

This application is a Streamlit-based tool for exploring events provided by the **Sympla Partners API**.

## Features

- Authenticate using your Sympla API token.
- Configure pagination and the number of events per page.
- Display event details in a compact, grid-style layout with three cards per row.
- Fetch event information such as:
  - Event name
  - Start and end dates
  - Event type
  - Discounts
  - Location (address, city, state, country)
  - Event URL
  - Event image
- Link to the official [Sympla Partners API documentation](https://developers.sympla.com.br/api-doc/partners/).

## Requirements

- Python 3.7+
- Libraries:
  - `streamlit`
  - `requests`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

### 5. Access the Application

Open the URL provided by Streamlit in your browser (usually `http://localhost:8501`).

## How to Use

1. **Authenticate**
   - Enter your Sympla API token in the sidebar.
2. **Set Parameters**
   - Choose the page number (`page`) and the number of events per page (`limit`) in the sidebar.
3. **Explore Events**
   - View events in a grid-style layout with detailed information for each event.

## Application Sections

### 1. **Introduction to Sympla API**
The app provides an overview of the Sympla Partners API, including its capabilities and a link to the [official documentation](https://developers.sympla.com.br/api-doc/partners/).

### 2. **Setup Section**
Configure the application parameters in the sidebar:
- **Token**: Your Sympla API access token.
- **Page**: The page number for paginated results.
- **Limit**: The number of events to display per page.

### 3. **Event Display**
Events are displayed as cards, organized in three columns. Each card contains:
- Event name
- Image (if available)
- Start and end dates
- Event type (e.g., `NORMAL`, `ONLINE`, `HYBRID`)
- Discount details (if applicable)
- Location
- Link to the event page

## Official Documentation

Learn more about the Sympla Partners API at the [official documentation page](https://developers.sympla.com.br/api-doc/partners/).

## Example Output

### Sidebar Configuration
- Token input
- Pagination setup (`page` and `limit`)

### Event Grid Layout
```
------------------------------------------------------------
| Event Card 1       | Event Card 2       | Event Card 3       |
------------------------------------------------------------
| Event Card 4       | Event Card 5       | Event Card 6       |
------------------------------------------------------------
```
Each card includes an image, event details, and a link to the event.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
