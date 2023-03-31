create schema if not exists MASSAGESTUDIO;
set search_path to MASSAGESTUDIO;

create table if not exists masseure (
    MA_ID  int generated always as identity primary key,
    MA_NAME text,
    
);


create table if not exists Zeitraster (
    RA_ID bigserial primary key,
    Zeit_von timestamp,
    Zeit_bis timestamp
);

create table if not exists patienten (
    patient_ID bigserial primary key,
    patient_Name text,
    patient_Vorname text,
    patient_Gebdate date,
    )

create table if not exists raum(
    raum_id bigserial primary key,
    raum_name text
)

