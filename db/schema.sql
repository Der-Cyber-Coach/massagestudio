create schema if not exists MASSAGESTUDIO;
set search_path to MASSAGESTUDIO;

create table if not exists MASSEUR (
    MA_ID  int generated always as identity primary key,
    MA_NAME text,
    
)