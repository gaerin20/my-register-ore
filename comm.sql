toc.dat                                                                                             0000600 0004000 0002000 00000002473 13775044761 0014463 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP       5                     y            gae_01     13.1 (Ubuntu 13.1-1.pgdg20.04+1)     13.1 (Ubuntu 13.1-1.pgdg20.04+1)                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                    0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                    0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                    1262    17195    gae_01    DATABASE     [   CREATE DATABASE gae_01 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'it_IT.UTF-8';
    DROP DATABASE gae_01;
                gae    false         	          0    17209    regore_committente 
   TABLE DATA           �   COPY public.regore_committente (id, nome, cognome, indirizzo, luogo, telefono, cellulare, email1, email2, codfisc, piva, referente) FROM stdin;
    public          gae    false    203       3081.dat            0    0    regore_committente_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.regore_committente_id_seq', 19, true);
          public          gae    false    202                                                                                                                                                                                                             3081.dat                                                                                            0000600 0004000 0002000 00000004254 13775044761 0014270 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        2	Siegfried	Unterberger	via S.Maria del Conforto 19A	39012 Merano	0473 272300 /16	0473 272300 /16	unterberger@pgumail.com	studio@pgumail.com	00171430218	00171430218	Siegfried Unterberger
3	Michael	Abler	np	Tirolo	np	np	abler@pgumail.com	abler@pgumail.com	np	np	Michael Abler
4	Condominio	Villa Meinhard	via Mainardo 140	39012 Merano	np	np	gaetano.rinaldo@poste.it	studio@pec.grinaldo.eu	91034670215	91034670215	Gaetano Rinaldo
5	Marco	Baricocchi	via Castello	Merano	0473	335 6522867	-@x.it	-@x.it	-	-	-
6	-	VEBA Invest srl	via S. Maria del Conforto 19A	39012 Merano	0473 272300	-	studio@pgumail.com	martin.zischg@pgumail.com	-	02346660216	Martin Zischg
7	Corona Ilario e Italo & Co	Magazzino Confezioni Hilary Sas	via Enrico Fermi 12	39012 Merano	0473	335	info@grinaldo.eu	info@grinaldo.eu	CRN	01208210219	Corona Ilario e Italo
9	Ilde	Turra	via Nazionale 32	39012 Merano	-	339 8645775	allessandrobrugnara@hotmail.com	allessandrobrugnara@hotmail.com	TRRLDI31P62F132W	-	Alessandro Brugnara
10	-	Terme Merano S.p.A.	piazza Terme 2	Merano	0473 252 000	335 7447640	info@thermemeran.it	stifter@thermemeran.it	-	00120820212	dott.ssa Adelheid Stifter
8	Cytiliving2.Me Srl	Cytiliving2.Me Srl	via S.Maria del Conforto 19 A	Merano	0473272300	0473272300	studio@pgumail.com	studio@pgumail.com	02983590213	02983590213	Martin
14	GSU Gmbh	GSU Gmbh	via S.Maria del Conforto 19 A	Merano	0473 272300	0473 272300	studio@pgumail.com	martin.zischg@pgumail.com	02601130210	02601130210	Martin Zischg
12	Cityliving2.Me Srl	Cityliving2.Me Srl	via S.Maria del Conforto 19 A	Merano	0473272300	-	studio@pgumail.com	studio@pgumail.com	-	02983590213	Martin
11	Cityliving - varianti acquirenti	Cityliving - varianti acquirenti	via S.Maria del Conforto 19 A	Merano	0473272300	-	studio@pgumail.com	studio@pgumail.com	02983590213	02983590213	Martin
1	Gaetano	Rinaldo	via Mainardo 140	39012 Merano	0473 445688	339 8174077	info@grinaldo.eu	gaetano_rinaldo@yahoo.it	RNLGTN60T18A952I	02528120211	Gaetano Rinaldo
15	Hansjorg	Beltrami	via Monastero	Merano	349 0553393	349 0553393	beltrami.hans@brennercom.net	beltrami.hans@brennercom.net	-	-	-
16	Laura	Speranza	via S.maria del Conforto	Merano	339 8171627	339 8171627	laura@noloso.it	laura@noloso.it	-	-	-
\.


                                                                                                                                                                                                                                                                                                                                                    restore.sql                                                                                         0000600 0004000 0002000 00000003452 13775044761 0015406 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1 (Ubuntu 13.1-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.1 (Ubuntu 13.1-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE gae_01;
--
-- Name: gae_01; Type: DATABASE; Schema: -; Owner: gae
--

CREATE DATABASE gae_01 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'it_IT.UTF-8';


ALTER DATABASE gae_01 OWNER TO gae;

\connect gae_01

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: regore_committente; Type: TABLE DATA; Schema: public; Owner: gae
--

COPY public.regore_committente (id, nome, cognome, indirizzo, luogo, telefono, cellulare, email1, email2, codfisc, piva, referente) FROM stdin;
\.
COPY public.regore_committente (id, nome, cognome, indirizzo, luogo, telefono, cellulare, email1, email2, codfisc, piva, referente) FROM '$$PATH$$/3081.dat';

--
-- Name: regore_committente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: gae
--

SELECT pg_catalog.setval('public.regore_committente_id_seq', 19, true);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      