create database if not exists turma;
use turma;
drop table if exists aluno;

create table aluno(
	id integer primary key auto_increment,
	nome varchar(50) not null,
	nota1 float not null,
	nota2 float not null);

INSERT INTO aluno VALUES (0, "LP", 4, 5);
INSERT INTO aluno VALUES (0, "Patrick", 7, 8);
INSERT INTO aluno VALUES (0, "Rafael", 8, 7);
INSERT INTO aluno VALUES (0, "Felipe", 9, 7);
