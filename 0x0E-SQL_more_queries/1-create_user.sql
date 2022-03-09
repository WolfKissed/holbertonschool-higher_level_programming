-- Creates a server user
CREATE LOGIN user_0d_1 WITH PASSWORD = 'user_0d_1_pwd';
GO 
CREATE USER user_0d_1 FOR LOGIN user_0d_1;  
GO
GRANT * to user_0d_1;
