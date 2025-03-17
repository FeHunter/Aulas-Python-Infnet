DROP DATABASE IF EXISTS infnet;
CREATE DATABASE infnet;
use infnet;
create table aluno (
    id_aluno int primary key auto_increment,
    nome_aluno varchar(50) not null
);
create table endereco (
    id_endereco int primary key auto_increment,
    rua varchar(50) not null,
    id_aluno int not null unique,
    foreign key (id_aluno) references aluno(id_aluno)
);
create table email (
    id_email int primary key auto_increment,
    mail varchar(50) not null,
    id_aluno int not null,
    foreign key (id_aluno) references aluno(id_aluno)
);
CREATE TABLE disciplina (
    id_disciplina INT NOT NULL AUTO_INCREMENT,
    nome_disciplina VARCHAR(30) NOT NULL,
    creditos INT NOT NULL,
    PRIMARY KEY (id_disciplina)
);
CREATE TABLE aluno_disciplina (
    id_aluno INT NOT NULL,
    id_disciplina INT NOT NULL,
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_disciplina) REFERENCES disciplina(id_disciplina)
);