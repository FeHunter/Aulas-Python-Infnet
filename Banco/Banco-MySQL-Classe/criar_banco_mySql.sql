create database if not exists banco;
use banco;

drop table if exists conta;

create table conta(
	id integer primary key auto_increment,
	nome varchar(50) not null,
	saldo float not null
);

INSERT INTO conta VALUES (0, "Leo", 100);
INSERT INTO conta VALUES (0, "Mateus", 200);
INSERT INTO conta VALUES (0, "Danilo", 300);
INSERT INTO conta VALUES (0, "Rafael", 400);
INSERT INTO conta VALUES (0, "Andre", 500);