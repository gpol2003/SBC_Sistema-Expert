llum(X) :-
    edifici_obert,
    habitacio_ocupada(X),
    not(llum_natural(X)).

ventilacio(X) :-
    edifici_obert,
    habitacio_ocupada(X),
    (not(habitacio_te_finestres(X)); not(temps_temperat)).

aire_condicionat(X) :-
    edifici_obert,
    habitacio_ocupada(X),
    temps_caluros,
    temperatura_ambient_superior_27(X).

calefaccio(X) :-
    edifici_obert,
    habitacio_ocupada(X),
    temps_fred,
    temperatura_ambient_inferior_19(X).

llum_natural(X) :-
    es_mati,
    habitacio_te_finestres(X).

es_mati :-
    hora(X),
    X > 9,
    X < 16.

edifici_obert :-
    dia_laborable,
    hora_de_treball.

dia_laborable :-
    dia(X),
    member(X, ['dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres']).

hora_de_treball :-
    hora(X),
    X > 8,
    X < 20.

temps_temperat :-
    not(clima_fred),
    not(clima_caluros).

temps_caluros :-
    clima_caluros.

temps_fred :-
    clima_fred.

clima_caluros :-
    temperatura(X),
    X >= 31.

clima_fred :-
    temperatura(X),
    X =< 17.

temperatura_ambient_superior_27(X) :-
    temperatura_ambient(X, Y),
    Y > 27.

temperatura_ambient_inferior_19(X) :-
    temperatura_ambient(X, Y),
    Y < 19.



% TEST 1
% En aquest text es per a comprovar que la llogica de les llums es correcte
habitacio_te_finestres(room1).
habitacio_ocupada(room1).
habitacio_ocupada(room2).

temperatura(23).
temperatura_ambient(room1, 14).
temperatura_ambient(room2, 25).
temperatura_ambient(room3, 15).

dia('dilluns').
hora(10).



% TEST 2
% En aquest test es per a comprovar que la llogica de la calefaccio es correcte
habitacio_te_finestres(room1).
habitacio_ocupada(room1).
habitacio_ocupada(room2).

temperatura(12).
temperatura_ambient(room1, 14).
temperatura_ambient(room2, 25).
temperatura_ambient(room3, 15).

dia('dimecres').
hora(10).



% TEST 3
% En aquest test es per a comprovar que la llogica de la aire_condicionat es correcte
habitacio_te_finestres(room1).
habitacio_ocupada(room1).
habitacio_ocupada(room2).

temperatura(31).
temperatura_ambient(room1, 14).
temperatura_ambient(room2, 28).
temperatura_ambient(room3, 28).

dia('dimarts').
hora(10).



% TEST 4
% Edifici tancat
habitacio_te_finestres(room1).
habitacio_ocupada(room1).
habitacio_ocupada(room2).

temperatura(31).
temperatura_ambient(room1, 14).
temperatura_ambient(room2, 28).
temperatura_ambient(room3, 28).

dia('diumenge').
hora(10).



% TEST 5
% Edifici tancat
habitacio_te_finestres(room1).
habitacio_ocupada(room1).
habitacio_ocupada(room2).

temperatura(31).
temperatura_ambient(room1, 14).
temperatura_ambient(room2, 28).
temperatura_ambient(room3, 28).

dia('dimecres').
hora(24).