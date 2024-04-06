# Backend Hiring Task API Documentation

This document provides information about the API endpoints for the Backend Hiring Task. The API is designed to manage student records in the system using FastAPI and MongoDB.

## Base URL

The base URL for all the API endpoints is yet to be defined in the `servers` section of the OpenAPI documentation.

## API Endpoints

### 1. Create Students

- **URL:** `/students`
- **Method:** `POST`
- **Description:** API to create a student in the system. All fields are mandatory and required while creating the student in the system.
- **Request Body:**
  ```json
  {
    "name": "string",
    "age": "integer",
    "address": {
      "city": "string",
      "country": "string"
    }
  }
  ```
- **Success Response:** `201` - A JSON response sending back the ID of the newly created student record.
- **Error Response:** `400` - Bad Request if the request body is not valid or if any required fields are missing.

### 2. List Students

- **URL:** `/students`
- **Method:** `GET`
- **Description:** An API to find a list of students. You can apply filters on this API by passing the query parameters as listed below.
- **Query Parameters:**
  - `country`: To apply filter of country. If not given or empty, this filter should be applied. (Optional)
  - `age`: Only records which have age greater than equal to the provided age should be present in the result. If not given or empty, this filter should be applied. (Optional)
- **Success Response:** `200` - A JSON array containing student records.
- **Error Response:** `400` - Bad Request if the query parameters are not valid.

### 3. Fetch Student

- **URL:** `/students/{id}`
- **Method:** `GET`
- **Description:** API to fetch a single student record based on the provided ID.
- **URL Parameters:**
  - `id`: The ID of the student previously created. (Required)
- **Success Response:** `200` - A JSON object containing the student record.
- **Error Response:** `404` - Not Found if the student record with the provided ID does not exist.

### 4. Update Student

- **URL:** `/students/{id}`
- **Method:** `PATCH`
- **Description:** API to update the student's properties based on information provided. Not mandatory that all information would be sent in PATCH, only what fields are sent should be updated in the Database.
- **URL Parameters:**
  - `id`: The ID of the student previously created. (Required)
- **Request Body:**
  ```json
  {
    "name": "string",
    "age": "integer",
    "address": {
      "city": "string",
      "country": "string"
    }
  }
  ```
- **Success Response:** `204` - No Content. The student record has been updated successfully.
- **Error Response:** `400` - Bad Request if the request body is not valid or if any required fields are missing. `404` - Not Found if the student record with the provided ID does not exist.

### 5. Delete Student

- **URL:** `/students/{id}`
- **Method:** `DELETE`
- **Description:** API to delete a student record based on the provided ID.
- **URL Parameters:**
  - `id`: The ID of the student previously created. (Required)
- **Success Response:** `200` - A JSON object indicating that the student record has been deleted successfully.
- **Error Response:** `404` - Not Found if the student record with the provided ID does not exist.