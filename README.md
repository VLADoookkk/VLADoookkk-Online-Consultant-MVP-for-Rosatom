#Марк закупщик
Телеграм бот для решения вопросов по закупкам.
https://t.me/robot_Mark_bot

##Программное решение ЧАТ БОТ «МАРК-ЗАКУПЩИК» МАРК-ЗАКУПЩИК представляет собой ЧАТ-Бот в Телеграмме, реализующий функцию проводника-помощника в вопросах закупок для сотрудников корпорации. Задача МАРКА генерировать ответы на вопросы по теме проведения закупочных процедур с высокой релевантностью ответов в виде диалога. Он построен на принципах клиентоцентричности, с учетом особенностей корпоративной культуры РосАтом. Чат-бот работает по принципу КВИЗов, ориентированных под конкретные жизненные ситуации. В решении задачи, мы применяли классические методы структуризации, кластеризации, а также использовали модель нейронной сети. Стек нашего решения: PYTHON, локальная языковая модель Llama 2 (LLM) для ответов на вопросы об их содержимом. Так же использована языковую модель MiniLM для интерпретации содержимого наших документов, которая сохраняет эту информацию в векторной базе данных, чтобы чат Марк закупщик имел к ней доступ. Интерпретированная информация сохраняется на диск. в формате файла FAISS  — векторной базе данных, оптимизированной для поиска схожих элементов в больших и многомерных наборах данных.
Решение основано на систематизации информации, позволяющее выдавать стандартные ответы на часто встречающие вопросы и при этом способное генерировать уникальные ответы на прочие запросы пользователей. Уникальность предлагаемого решения, это мгновенная обработка вопросов на основе уникального алгоритма, который позволяет получить наиболее полный и релевантный ответ.

###Используемые инструменты для бота:
python 3.10
langchain
 sentence_transformers 
faiss-cpu
 ctransformers
aiogram==2.14.2
llama-2-7b-chat.ggmlv3.q8_0
