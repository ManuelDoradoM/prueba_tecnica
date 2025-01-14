Car Rental API
This project is a RESTful API for managing car rentals. It provides two endpoints:

    GET endpoint to list available cars on a specific date.

    POST endpoint to create a car reservation for a specific date range.

The API includes logging for request tracking and a unit test.

Features

    List Available Cars: Retrieve a list of cars available for rent on a given date.

    Create Reservations: Book a car for a specific date range.

    Logging: Tracks API activity and errors.

    Unit Tests: Verifies the correctness of the API endpoint '/available_cars'.

Technologies Used
    FastAPI: A modern web framework for building APIs with Python.

    Pydantic: Data validation and settings management.

    Logging: Integrated Python logging for request tracking.

    Pytest: Framework for unit testing.


Installation and Setup

Clone the repository:

    git clone https://github.com/your-repository/car-rental-api.git
    cd car-rental-api


Activate a virtual environment:

    venv\Scripts\activate


Install dependencies:

    pip install -r requirements.txt


Run the application:

    uvicorn main:app --reload

    Access the API documentation: Open your browser and navigate to http://127.0.0.1:8000/docs for the Swagger UI or http://127.0.0.1:8000/redoc for ReDoc.

    Logs are storage in a file /logger/utils/logs/app.log

Run tests:

    pytest .\tests\test_availables_cars.py

Future Improvements

Model-Based Reservations

    Transition from reserving specific cars to allowing reservations by car models.

    Automatically assign an available car of the selected model for the reservation.

Advanced Search Filters

    Add filters to enhance the car search functionality, such as:
        Model: Search by specific car models.
        
        Seating Capacity: Filter cars by the number of seats.

        Fuel Type: Choose between petrol, diesel, electric, or hybrid.

        Transmission Type: Filter by automatic or manual gearbox.

        Features:
            Proximity sensors.
            Rearview camera.

Improved User Experience

    Add sorting options for results (e.g., price, availability, fuel efficiency).
    
    Provide detailed car specifications and images in the search results.