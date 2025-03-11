# Freebie Tracker App

## Introduction
This project involves building a Freebie Tracker App for developers attending hackathons. The app will help developers keep track of the free items (freebies) they receive. The application is built using Python with SQLAlchemy to manage the database relationships.

The app consists of three models:
- **Company**: A company that gives out freebies.
- **Dev**: A developer who collects freebies.
- **Freebie**: Represents a free item given by a company to a developer.

A **Company** has many **Freebies**, a **Dev** has many **Freebies**, and a **Freebie** belongs to both a **Dev** and a **Company**. The relationship between **Company** and **Dev** is a many-to-many relationship.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python (3.x recommended)
- pipenv (for dependency management)
- SQLAlchemy (ORM for database management)

### Installation
Clone the repository and navigate to the project directory:
```sh
$ git clone <repository-url>
$ cd freebie-tracker-app
```

Install dependencies and activate the virtual environment:
```sh
$ pipenv install && pipenv shell
```

## Instructions
1. **Migrate the Database**
   - Create the `freebies` table with necessary attributes and foreign keys.
   - Run the migrations using SQLAlchemy.

2. **Seed the Database**
   - Populate the database with sample data using `seed.py`.

3. **Test the App**
   - Run the debug tool to test the implemented methods:
   ```sh
   $ python debug.py
   ```
   - Use the interactive shell to check object relationships and methods.

4. **Implement Methods**
   - Follow the deliverables list to implement and test methods for the models.
   - Ensure relationships are correctly established.

## Database Schema

### `companies` Table
| Column         | Type   |
|---------------|--------|
| name          | String |
| founding_year | Integer |

### `devs` Table
| Column | Type   |
|--------|--------|
| name   | String |

### `freebies` Table
| Column    | Type    |
|-----------|---------|
| item_name | String  |
| value     | Integer |
| dev_id    | ForeignKey (devs.id) |
| company_id| ForeignKey (companies.id) |

## Relationships & Methods

### Freebie
- `Freebie.dev`: Returns the Dev instance associated with the freebie.
- `Freebie.company`: Returns the Company instance associated with the freebie.
- `Freebie.print_details()`: Returns a formatted string: `{dev name} owns a {freebie item_name} from {company name}`.

### Company
- `Company.freebies`: Returns all freebies given by the company.
- `Company.devs`: Returns all developers who collected freebies from the company.
- `Company.give_freebie(dev, item_name, value)`: Creates a new Freebie instance associated with the company and the given developer.
- `Company.oldest_company()`: Returns the company with the earliest founding year.

### Dev
- `Dev.freebies`: Returns all freebies collected by the developer.
- `Dev.companies`: Returns all companies the developer has received freebies from.
- `Dev.received_one(item_name)`: Returns `True` if the developer has received a freebie with the given item_name, otherwise `False`.
- `Dev.give_away(dev, freebie)`: Transfers a freebie from one developer to another if the freebie belongs to the giving developer.

## Debugging and Testing
- Run the debug session:
```sh
$ python debug.py
```
- Use the interactive shell to create instances and test relationships.

## Best Practices
- Focus on **error-free code** before completing all deliverables.
- Test your code frequently in the console.
- Prioritize working code over clean code; refactor later if time allows.
- Leave comments if methods are incomplete.

## Submission
Before submitting:
- Ensure all required methods are implemented and functional.
- Run and verify that your code works as expected.
- Comment on any incomplete or non-working methods explaining your progress.

## Author
Developed as part of a Moringa School student Project by Kairu Maina.

## License
This project is licensed under the MIT License.

