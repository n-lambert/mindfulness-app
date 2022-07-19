--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: activities; Type: TABLE; Schema: public; Owner: nicole
--

CREATE TABLE public.activities (
    activity_id integer NOT NULL,
    user_id integer,
    activity_idea text
);


ALTER TABLE public.activities OWNER TO nicole;

--
-- Name: activities_activity_id_seq; Type: SEQUENCE; Schema: public; Owner: nicole
--

CREATE SEQUENCE public.activities_activity_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.activities_activity_id_seq OWNER TO nicole;

--
-- Name: activities_activity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicole
--

ALTER SEQUENCE public.activities_activity_id_seq OWNED BY public.activities.activity_id;


--
-- Name: journal_responses; Type: TABLE; Schema: public; Owner: nicole
--

CREATE TABLE public.journal_responses (
    journal_response_id integer NOT NULL,
    user_id integer,
    date date,
    response text
);


ALTER TABLE public.journal_responses OWNER TO nicole;

--
-- Name: journal_responses_journal_response_id_seq; Type: SEQUENCE; Schema: public; Owner: nicole
--

CREATE SEQUENCE public.journal_responses_journal_response_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.journal_responses_journal_response_id_seq OWNER TO nicole;

--
-- Name: journal_responses_journal_response_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicole
--

ALTER SEQUENCE public.journal_responses_journal_response_id_seq OWNED BY public.journal_responses.journal_response_id;


--
-- Name: survey_answers; Type: TABLE; Schema: public; Owner: nicole
--

CREATE TABLE public.survey_answers (
    survey_answer_id integer NOT NULL,
    user_id integer,
    date date,
    q1 integer,
    q2 integer,
    q3 integer,
    q4 integer,
    q5 integer
);


ALTER TABLE public.survey_answers OWNER TO nicole;

--
-- Name: survey_answers_survey_answer_id_seq; Type: SEQUENCE; Schema: public; Owner: nicole
--

CREATE SEQUENCE public.survey_answers_survey_answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.survey_answers_survey_answer_id_seq OWNER TO nicole;

--
-- Name: survey_answers_survey_answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicole
--

ALTER SEQUENCE public.survey_answers_survey_answer_id_seq OWNED BY public.survey_answers.survey_answer_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: nicole
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying,
    password character varying,
    name character varying
);


ALTER TABLE public.users OWNER TO nicole;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: nicole
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO nicole;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicole
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: activities activity_id; Type: DEFAULT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.activities ALTER COLUMN activity_id SET DEFAULT nextval('public.activities_activity_id_seq'::regclass);


--
-- Name: journal_responses journal_response_id; Type: DEFAULT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.journal_responses ALTER COLUMN journal_response_id SET DEFAULT nextval('public.journal_responses_journal_response_id_seq'::regclass);


--
-- Name: survey_answers survey_answer_id; Type: DEFAULT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.survey_answers ALTER COLUMN survey_answer_id SET DEFAULT nextval('public.survey_answers_survey_answer_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: activities; Type: TABLE DATA; Schema: public; Owner: nicole
--

COPY public.activities (activity_id, user_id, activity_idea) FROM stdin;
1	1	Take a bath
2	1	Take a bath
3	1	Watch a movie
4	2	Read a newspaper or magazine
5	2	Take photographs
6	2	Take photographs
7	3	Read a newspaper or magazine
8	3	Listen to music
9	3	Take a bath
10	4	Take photographs
11	4	Take a bath
12	4	Go for a walk
13	5	Read a newspaper or magazine
14	5	Take photographs
15	5	Laugh
16	6	Read a newspaper or magazine
17	6	Take photographs
18	6	Laugh
19	7	Sit in the sun
20	7	Laugh
21	7	Listen to music
22	8	Take photographs
23	8	Laugh
24	8	Read a newspaper or magazine
25	9	Take a bath
26	9	Watch a movie
27	9	Read a newspaper or magazine
28	10	Go for a walk
29	10	Sit in the sun
30	10	Take a bath
31	11	Sitting in the sun
32	11	Reading a good book
33	11	Play board games
34	12	Play video games
35	12	Listen to music
36	12	Watch Youtube
37	13	Hikes
38	13	Tennis
39	13	Playing video games
40	14	Listen to music
41	14	Draw
42	14	Watch Youtube
43	15	reading a book
44	15	taking a bath
45	15	playing games
46	16	Playing video games
47	16	Watching Youtube
48	16	Listening to music
49	17	Learning a new hobby
50	17	Taking a run
51	17	Star-gazing
52	18	Reading a book
53	18	Taking a bath
54	18	Walking in the rain
\.


--
-- Data for Name: journal_responses; Type: TABLE DATA; Schema: public; Owner: nicole
--

COPY public.journal_responses (journal_response_id, user_id, date, response) FROM stdin;
1	1	2022-06-29	My journal entry
2	2	2022-06-29	My journal entry
3	3	2022-06-29	My journal entry
4	4	2022-06-29	My journal entry
5	5	2022-06-29	My journal entry
6	6	2022-06-29	My journal entry
7	7	2022-06-29	My journal entry
8	8	2022-06-29	My journal entry
9	9	2022-06-29	My journal entry
10	10	2022-06-29	My journal entry
12	12	2022-06-29	my little brother
13	12	2022-06-29	my little brother
14	12	2022-06-29	my little brother
15	12	2022-06-29	my little brother
16	12	2022-06-29	my little brother
17	12	2022-06-29	little brother
18	12	2022-06-29	little brother
19	12	2022-06-29	my little brother
20	11	2022-06-30	Nervous that my data graph won't work, but excited to get it to work because I think it will elevate my project.
21	13	2022-06-30	Just kidding my day turned around.
22	11	2022-07-05	Today I am hoping to have a dynamic data chart that shows what the survey answers were based off the day for each user.
23	14	2022-07-05	Walk through success!
24	11	2022-07-06	Today I am hoping to standardize my chart.js
25	15	2022-07-06	thank you for helping Amy
26	11	2022-07-07	Hoping to add my last new feature which is turning the radio buttons into a range drag bar
11	11	2022-06-29	Still trying to find the right verbiage for how to flash a mindfulness activity without it sounding rude or pretentious. Coming up, I need to add the slide bars to my survey.html. Maybe I don't want to add the slide bars
27	16	2022-07-07	this is a test
28	16	2022-07-07	testing testing
29	1	2022-07-07	
30	2	2022-07-07	
31	12	2022-07-07	First test using all of the slider buttons
32	11	2022-07-11	start of styling... so far looking into modals... so will this still work?
33	17	2022-07-11	tests tests tests... so lets see if it works
34	11	2022-07-12	day 2 of official styling, example of showing ione a modal
35	14	2022-07-12	advising walk through... showing modals
37	16	2022-07-13	      today is going to be a good day
36	11	2022-07-13	I need to write text, watch this
38	11	2022-07-14	      today we are talking about aws and I am excited but also am in the head space of needing to finish styling my project.
40	16	2022-07-15	            testing the flash message if its a bad day
41	11	2022-07-18	            Today is the first day we haven't had an official lecture, and it's honestly pretty strange. I hope to start and finish my read-me today as well as create a cover letter template and get my script approved.
39	11	2022-07-15	            Officially done with styling and working on my script. Here is a demo of how it works
42	18	2022-07-18	            demo time!
\.


--
-- Data for Name: survey_answers; Type: TABLE DATA; Schema: public; Owner: nicole
--

COPY public.survey_answers (survey_answer_id, user_id, date, q1, q2, q3, q4, q5) FROM stdin;
1	1	2022-06-29	1	5	3	5	3
2	2	2022-06-29	3	1	3	2	2
3	3	2022-06-29	2	1	2	5	4
4	4	2022-06-29	3	4	1	1	1
5	5	2022-06-29	4	2	3	4	5
6	6	2022-06-29	4	3	3	2	3
7	7	2022-06-29	1	4	4	1	1
8	8	2022-06-29	5	5	4	4	5
9	9	2022-06-29	5	2	5	2	3
10	10	2022-06-29	2	3	5	5	5
11	11	2022-06-29	3	3	3	3	3
12	12	2022-06-29	4	1	1	1	2
13	12	2022-06-29	2	5	5	5	5
14	12	2022-06-29	2	5	5	5	5
15	12	2022-06-29	2	5	5	5	5
16	12	2022-06-29	2	5	5	5	5
17	12	2022-06-29	5	5	5	5	5
18	12	2022-06-29	5	5	5	5	5
19	12	2022-06-29	5	5	5	5	5
20	11	2022-06-30	3	3	4	5	5
21	13	2022-06-30	1	5	5	5	5
22	11	2022-07-05	4	3	3	4	4
23	14	2022-07-05	2	2	2	2	2
24	11	2022-07-06	4	5	3	1	2
25	15	2022-07-06	3	3	3	3	3
26	11	2022-07-07	4	5	3	5	1
27	16	2022-07-07	4	5	1	2	4
28	16	2022-07-07	1	2	2	2	2
29	1	2022-07-07	3	1	1	1	1
30	2	2022-07-07	3	2	2	2	2
31	12	2022-07-07	1	2	3	4	5
32	11	2022-07-11	4	3	2	1	2
33	17	2022-07-11	2	4	3	2	4
34	11	2022-07-12	4	2	4	2	3
35	14	2022-07-12	4	3	2	4	2
36	11	2022-07-13	3	3	3	3	3
37	16	2022-07-13	4	3	4	2	5
38	11	2022-07-14	4	5	1	4	2
39	11	2022-07-15	5	2	1	4	3
40	16	2022-07-15	1	1	1	1	1
41	11	2022-07-18	4	1	2	5	2
42	18	2022-07-18	4	2	4	5	5
43	11	2022-07-17	1	2	4	5	4
44	11	2022-07-16	3	4	2	2	5
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: nicole
--

COPY public.users (user_id, email, password, name) FROM stdin;
1	user0@test.com	test	user0
2	user1@test.com	test	user1
3	user2@test.com	test	user2
4	user3@test.com	test	user3
5	user4@test.com	test	user4
6	user5@test.com	test	user5
7	user6@test.com	test	user6
8	user7@test.com	test	user7
9	user8@test.com	test	user8
10	user9@test.com	test	user9
11	nicole@test.com	test	Nicole
12	brayden@test.com	test	Brayden
13	dan@test.com	test	Dan
14	ione@test.com	test	Ione
15	amy@test.com	test	Amy
16	colton@test.com	test	Colton
17	cookie@test.com	test	Cookie
18	nicole@demo.com	demo	Nicole
\.


--
-- Name: activities_activity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicole
--

SELECT pg_catalog.setval('public.activities_activity_id_seq', 54, true);


--
-- Name: journal_responses_journal_response_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicole
--

SELECT pg_catalog.setval('public.journal_responses_journal_response_id_seq', 42, true);


--
-- Name: survey_answers_survey_answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicole
--

SELECT pg_catalog.setval('public.survey_answers_survey_answer_id_seq', 44, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicole
--

SELECT pg_catalog.setval('public.users_user_id_seq', 18, true);


--
-- Name: activities activities_pkey; Type: CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.activities
    ADD CONSTRAINT activities_pkey PRIMARY KEY (activity_id);


--
-- Name: journal_responses journal_responses_pkey; Type: CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.journal_responses
    ADD CONSTRAINT journal_responses_pkey PRIMARY KEY (journal_response_id);


--
-- Name: survey_answers survey_answers_pkey; Type: CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.survey_answers
    ADD CONSTRAINT survey_answers_pkey PRIMARY KEY (survey_answer_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: activities activities_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.activities
    ADD CONSTRAINT activities_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: journal_responses journal_responses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.journal_responses
    ADD CONSTRAINT journal_responses_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: survey_answers survey_answers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicole
--

ALTER TABLE ONLY public.survey_answers
    ADD CONSTRAINT survey_answers_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

