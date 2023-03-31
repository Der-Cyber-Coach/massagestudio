create schema if not exists MASSAGESTUDIO;
set search_path to MASSAGESTUDIO;

create table if not exists masseure (
    MA_ID  int generated always as identity primary key,
    MA_NAME text,
    
);


create table if not exists Zeitraster (
    ZR_ID bigserial primary key,
    Zeit_von timestamp,
    Zeit_bis timestamp
);

create table if not exists patienten (
    pa_ID bigserial primary key,
    patient_Name text,
    patient_Vorname text,
    patient_Gebdate date,
    );

create table if not exists raum(
    ra_id bigserial primary key,
    raum_name text
);

create table if not exists behandlungsart(
    be_id bigserial primary key
    be_name text,
    be_dauer int,
    be_preis int,
    be_beschreibung text,

);


create table if not exists termin(
    te_id bigserial primary key,
    te_datum date,
    constraint fk_te_pa_id foreign key (pa_id) references patienten(pa_id),
    constraint fk_te_ma_id foreign key (ma_id) references masseure(ma_id),
    constraint fk_te_be_id foreign key (be_id) references behandlungsart(be_id),
    constraint fk_te_ra_id foreign key (ra_id) references raum(ra_id),
    constraint fk_te_ZA_id foreign key (ZA_id) references Zeitraster(ZA_id),
);
