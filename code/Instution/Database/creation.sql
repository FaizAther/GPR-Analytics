-- Comments
CREATE TABLE University (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    admin numeric NOT NULL,
    foreign key (admin) references User(id)
);

CREATE TABLE Faculty (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    university numeric NOT NULL,
    dean numeric NOT NULL,
    foreign key (university) references University(id),
    foreign key (dean) references User(id)
);

CREATE TABLE Course (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    coordinator NOT NULL, 
    foreign key (coordinator) references User(id),
    primary key (id)
);

CREATE TABLE Event (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    manager NOT NULL, 
    foreign key (manager) references User(id),
    primary key (id)
);

CREATE TABLE Attendance (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    authority NOT NULL,
    foreign key (authority) references User(id),
    primary key (id)
);

CREATE TABLE User (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    password text NOT NULL
);
