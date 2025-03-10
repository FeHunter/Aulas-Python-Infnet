.open turma.db
.mode table

drop table if exists aluno;

create table aluno(
	id integer primary key autoincrement,
	nome char(50) not null,
	nota1 real not null,
	nota2 real not null
);

INSERT INTO aluno VALUES (null, 'LP', 4, 5);
INSERT INTO aluno VALUES (null, 'Felipe', 7, 8);
INSERT INTO aluno VALUES (null, 'Patrick', 8, 7);
INSERT INTO aluno VALUES (null, 'Rafael', 7, 9);
