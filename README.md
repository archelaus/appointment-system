# Flask Doctor Appointment System

This is a simple Flask project that provides a basic RESTful API for managing doctor appointments. The application allows users to retrieve a list of doctors, obtain information about a specific doctor, and book appointments with doctors.

## Setup

1. Make sure you have Python installed on your machine.

2. Install the required dependencies by running the following command in your terminal:

   ```bash
   pip install Flask
   ```

3. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/archelaus/flask-doctor-appointment.git
   ```

4. Navigate to the project directory:

   ```bash
   cd flask-doctor-appointment
   ```

5. Run the Flask application:

   ```bash
   python app.py
   ```

   The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Endpoints

### 1. List Doctors

- **Endpoint:** `/doctors`
- **Method:** `GET`
- **Description:** Retrieve a list of doctors.

### 2. Doctor Information

- **Endpoint:** `/doctors/<int:id>`
- **Method:** `GET`
- **Description:** Retrieve information about a specific doctor by providing their ID.

### 3. Book Appointment

- **Endpoint:** `/book`
- **Method:** `POST`
- **Description:** Book an appointment with a doctor.

  - **Parameters:**

    - `id` (int): Doctor's ID.
    - `day` (string): Appointment day (Monday-Saturday).
    - `time` (string): Appointment time (15:00-21:00).

  - **Example Request:**

    ```bash
    curl -X POST -d "id=23&day=Monday&time=15:00" http://127.0.0.1:5000/book
    ```

  - **Example Response:**

    ```
    Your appointment with Dr. Shaun Murphy for Monday at 15:00 has been successfully booked.
    ```

    or

    ```
    Invalid day selected. Please pick a day between Monday-Saturday.
    ```

## Notes

- The application uses in-memory data for demonstration purposes. In a real-world scenario, you would replace this with a database.

- Make sure to handle security considerations (e.g., input validation, authentication, and authorization) before deploying this application in a production environment.
