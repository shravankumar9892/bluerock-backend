-- Queries to fill up the tables
select * from `bluerock_products`.`products`;

-- Queries to create all the tables
CREATE TABLE `bluerock_products`.`cat2` (
  `id` INT PRIMARY KEY,
  `cat2` VARCHAR(120) NULL,
  `id_cat1` INT,
  FOREIGN KEY (id_cat1) REFERENCES `bluerock_products`.`cat1` (`id`)
);

drop table cat1;

create table `bluerock_products`.`cat1` (
	`id` int primary key,
    `cat1` varchar(120) null
) comment = 'Contains the topmost categories of the products';

create table `bluerock_products`.`cat3` (
	`id` int primary key,
    `cat3` varchar (120) null,
    `id_cat1` INT,
    `id_cat2` INT,
    foreign key (id_cat1) references `bluerock_products`.`cat1` (`id`),
    foreign key (id_cat2) references `bluerock_products`.`cat2` (`id`)
) comment = 'Contains category 3 of the products';

create table `bluerock_products`.`cat4` (
	`id` int primary key,
    `cat4` varchar (120) null,
    `id_cat1` INT,
    `id_cat2` INT,
    `id_cat3` int,
    foreign key (id_cat1) references `bluerock_products`.`cat1` (`id`),
    foreign key (id_cat2) references `bluerock_products`.`cat2` (`id`),
    foreign key (id_cat3) references `bluerock_products`.`cat3` (`id`)
) comment = 'Contains category 4 of the products';

create table `bluerock_products`.`cat4` (
	`id` int primary key,
    `cat4` varchar (120) null,
    `id_cat1` INT,
    `id_cat2` INT,
    `id_cat3` int,
    foreign key (id_cat1) references `bluerock_products`.`cat1` (`id`),
    foreign key (id_cat2) references `bluerock_products`.`cat2` (`id`),
    foreign key (id_cat3) references `bluerock_products`.`cat3` (`id`)
) comment = 'Contains category 4 of the products';

create table `bluerock_products`.`products` (
	`id` int primary key,
    `title` varchar (120) null,
    `description` varchar (120) null,
    `price` int,
    `discount` int,
    `image` varchar (120) null,
    `id_cat4` int,
    foreign key (id_cat4) references `bluerock_products`.`cat4` (`id`)
) comment = 'Contains all the product details in this table';