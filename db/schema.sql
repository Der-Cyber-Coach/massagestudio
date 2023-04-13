create schema if not exists massagestudio;
set search_path to massagestudio;

create table if not exists masseure (
    MA_ID  int generated always as identity primary key,
    MA_NAME text
    
);

create table if not exists patienten (
pa_id bigserial primary key,
pa_name text);