create table tbl_Autor (
ID_Autor int not null generated always as identity,
Nome_Autor varchar(50) not null,
Sobrenome varchar,
Data_Nasc date,
primary key (ID_Autor)
)


create table tbl_Livro(
ID_Livro int not null generated always as identity,
Nome_Livro varchar(50),
ID_Autor int not null,
ID_Editoraint int not null,
Data_Publicacao date,
Genero varchar not null,
NumPaginas int,
primary key (ID_Livro),
foreign key (ID_Autor) references tbl_Autor (ID_Autor)
)

create table tbl_Editora(
ID_Editora int not null,
Nome_Editora varchar (50),
primary key (ID_Editora)
)

create table tbt_loja(
ID_Loja int not null generated always as identity,
nome_loja varchar(50) not null,
cidade_loja varchar(50) not null,
ID_livro int not null,

foreign key (ID_Livro) references tbt_Livro(ID_Livro),

)
