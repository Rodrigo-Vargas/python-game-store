# Game store management

## Admin Features
 - Admin should be able to add a game with required fields: name, price, genre.
 - Admin should be able to edit an existing game.
 - Admin should be able to delete a game.
 - Admin should be able to add a user.
 - Admin should be able to edit a user’s details (e.g. name, balance).
 - Admin should be able to delete a user.
 - Admin should be able to generate a report of top-selling games (by sales volume).
 - Admin should be able to generate a report of total revenue.
 - Admin should be able to generate a report of user activity (e.g. games purchased, refunded).

## User Features
 - User should be able to browse available games.
 - User should be able to buy a game.
 - User should not be able to buy a game twice.
 - User should be able to refund a game they purchased.
 - User cannot refund games they don’t own.
 - User cannot purchase a game without sufficient balance.
 - User should be able to add credits to their wallet.
 - User should be able to view their purchase history.
 - User should be able to see the “Game of the Day” featured on the home screen.

## Game Attributes
 - A game should have a name (string), price (float), and genre (string).
 - Games should have a unique identifier (e.g., UUID or auto-incremented ID).

## User Attributes
 - A user should have a name (string), and a balance (float).
 - Users should have a unique identifier.
 - Users should have a library of owned games.

## Persistence & Storage
 - All user, game, and transaction data must be persisted.
 - The application should allow choosing between JSON and SQLite for data storage.
 - If JSON is used, it must handle file read/write safely (with locking or atomic writes).
 - If SQLite is used, it must ensure data integrity (e.g., use transactions for purchases/refunds).

## Suggested Additions
 - User login system (admin vs. normal user, for permissions)
 - Game availability status (active/inactive) to support soft deletion
 - Date tracking (e.g., purchase date, refund date) using datetime
 - Logging system to record all transactions and admin operations
 - Pagination or filtering support for game browsing (by genre, price, etc.)
 - Display user current balance on main screen