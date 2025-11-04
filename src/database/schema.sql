CREATE TYPE StatusType AS ENUM ('deleted', 'completed', 'in-progress', 'pending');

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name text NOT NULL,
    email text UNIQUE,
    password text,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);

CREATE TABLE todos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID, 
  title text NOT NULL,
  description text,
  due_date timestamp,
  status StatusType DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE  );

CREATE TABLE sub_todo (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title text NOT NULL,
  description text,
  due_date timestamp,
  status StatusType DEFAULT 'pending',
  todo_id UUID,  
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP,
  FOREIGN KEY (todo_id) REFERENCES todos(id) ON DELETE CASCADE
  );

