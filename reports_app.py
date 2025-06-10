import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Конфигурация страницы
st.set_page_config(
    page_title="Система управления отчетами",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Инициализация данных в session_state
if 'reports_data' not in st.session_state:
    st.session_state.reports_data = [
        {
            'id': 1,
            'name': 'Финансовый отчет Q1',
            'department': 'Финансы',
            'owner': 'Иванов И.И.',
            'status': 'Актуальный',
            'last_update': datetime.now() - timedelta(days=5),
            'next_update': datetime.now() + timedelta(days=25),
            'completion': 95
        },
        {
            'id': 2,
            'name': 'Отчет по продажам',
            'department': 'Продажи',
            'owner': 'Петров П.П.',
            'status': 'Требует обновления',
            'last_update': datetime.now() - timedelta(days=35),
            'next_update': datetime.now() + timedelta(days=5),
            'completion': 70
        },
        {
            'id': 3,
            'name': 'HR отчет',
            'department': 'HR',
            'owner': 'Сидорова С.С.',
            'status': 'Актуальный',
            'last_update': datetime.now() - timedelta(days=10),
            'next_update': datetime.now() + timedelta(days=20),
            'completion': 100
        }
    ]

if 'feedback_data' not in st.session_state:
    st.session_state.feedback_data = []

if 'admin_mode' not in st.session_state:
    st.session_state.admin_mode = False

# Боковая панель навигации
st.sidebar.title("📊 Система управления отчетами")

# Кнопка админ панели
if st.sidebar.button("🔧 Админ панель", key="admin_toggle"):
    st.session_state.admin_mode = not st.session_state.admin_mode

# Основные страницы
main_pages = [
    "📋 Инструкции по отчетам",
    "⚡ Действия с отчетами", 
    "🏷️ Атрибуты и термины",
    "📈 Дашборд актуальности",
    "🤖 Задать вопрос",
    "💬 Обратная связь"
]

# Админ страницы
admin_pages = [
    "🔍 Контроль публикации",
    "📊 Статистика публикации", 
    "⚠️ Проблемные вопросы"
]

# Выбор страницы
if st.session_state.admin_mode:
    all_pages = main_pages + ["---"] + admin_pages
else:
    all_pages = main_pages

selected_page = st.sidebar.selectbox("Выберите страницу:", all_pages)

# Основной контент
if selected_page == "📋 Инструкции по отчетам":
    st.title("📋 Инструкции по отчетам")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Документация", "📝 Шаблоны", "🚀 С чего начать", "❓ Частые вопросы"])
    
    with tab1:
        st.header("Документация")
        st.markdown("""
        ### Общие принципы работы с отчетами
        
        1. **Структура отчета**: Каждый отчет должен содержать четкую структуру с заголовками и подразделами
        2. **Периодичность**: Определите частоту обновления отчета
        3. **Ответственность**: Назначьте владельца отчета
        4. **Атрибуты**: Заполните все необходимые метаданные
        
        ### Жизненный цикл отчета
        - Создание → Наполнение → Проверка → Публикация → Актуализация
        """)
        
        with st.expander("Подробные требования"):
            st.markdown("""
            - Отчет должен быть актуализирован не реже чем раз в месяц
            - Все данные должны быть верифицированы  
            - Обязательно указание источников данных
            - Соответствие корпоративным стандартам оформления
            """)
    
    with tab2:
        st.header("Шаблоны отчетов")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Финансовые отчеты")
            st.download_button(
                label="Скачать шаблон финансового отчета",
                data="Шаблон финансового отчета (заглушка)",
                file_name="financial_report_template.xlsx",
                mime="application/vnd.ms-excel"
            )
            
            st.subheader("📈 Отчеты по продажам")
            st.download_button(
                label="Скачать шаблон отчета по продажам", 
                data="Шаблон отчета по продажам (заглушка)",
                file_name="sales_report_template.xlsx",
                mime="application/vnd.ms-excel"
            )
        
        with col2:
            st.subheader("👥 HR отчеты")
            st.download_button(
                label="Скачать шаблон HR отчета",
                data="Шаблон HR отчета (заглушка)", 
                file_name="hr_report_template.xlsx",
                mime="application/vnd.ms-excel"
            )
            
            st.subheader("🔧 Операционные отчеты")
            st.download_button(
                label="Скачать операционный шаблон",
                data="Шаблон операционного отчета (заглушка)",
                file_name="operations_report_template.xlsx", 
                mime="application/vnd.ms-excel"
            )
    
    with tab3:
        st.header("🚀 С чего начать")
        
        st.markdown("""
        ### Пошаговый план создания отчета:
        
        **Шаг 1: Планирование**
        - Определите цель отчета
        - Выберите целевую аудиторию
        - Установите периодичность обновления
        
        **Шаг 2: Подготовка**
        - Скачайте подходящий шаблон
        - Соберите необходимые данные
        - Определите источники информации
        
        **Шаг 3: Создание**
        - Заполните базовую информацию
        - Добавьте метаданные и атрибуты
        - Настройте автоматизацию (при необходимости)
        
        **Шаг 4: Публикация**
        - Проверьте отчет на соответствие требованиям
        - Получите одобрение руководителя
        - Опубликуйте отчет в системе
        """)
        
        st.info("💡 **Совет**: Начните с простого отчета и постепенно усложняйте его структуру")
    
    with tab4:
        st.header("❓ Частые вопросы")
        
        with st.expander("Как часто нужно обновлять отчет?"):
            st.write("Частота обновления зависит от типа отчета. Финансовые отчеты - ежемесячно, операционные - еженедельно.")
        
        with st.expander("Кто может быть владельцем отчета?"):
            st.write("Владельцем может быть любой сотрудник, имеющий доступ к необходимым данным и ответственность за их актуальность.")
        
        with st.expander("Что делать, если отчет не актуализируется вовремя?"):
            st.write("Система автоматически уведомляет владельца. Если проблема критична, обратитесь к администратору.")
        
        with st.expander("Как настроить автоматизацию отчета?"):
            st.write("Используйте раздел 'Действия с отчетами' → 'Автоматизировать'. Выберите источник данных и периодичность.")

elif selected_page == "⚡ Действия с отчетами":
    st.title("⚡ Действия с отчетами")
    
    action = st.selectbox(
        "Выберите действие:",
        ["Зарегистрировать новый", "Обновить существующий", "Сменить владельца", "Автоматизировать"]
    )
    
    if action == "Зарегистрировать новый":
        st.subheader("📝 Регистрация нового отчета")
        
        with st.form("new_report_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                report_name = st.text_input("Название отчета *")
                department = st.selectbox("Департамент *", ["Финансы", "Продажи", "HR", "ИТ", "Операции"])
                owner = st.text_input("Владелец отчета *")
                
            with col2:
                report_type = st.selectbox("Тип отчета", ["Финансовый", "Операционный", "Аналитический", "Статистический"])
                frequency = st.selectbox("Периодичность обновления", ["Еженедельно", "Ежемесячно", "Ежеквартально", "По запросу"])
                priority = st.selectbox("Приоритет", ["Высокий", "Средний", "Низкий"])
            
            description = st.text_area("Описание отчета")
            
            submit_button = st.form_submit_button("Зарегистрировать отчет")
            
            if submit_button:
                if report_name and department and owner:
                    new_report = {
                        'id': len(st.session_state.reports_data) + 1,
                        'name': report_name,
                        'department': department,
                        'owner': owner,
                        'status': 'Новый',
                        'last_update': datetime.now(),
                        'next_update': datetime.now() + timedelta(days=30),
                        'completion': 0
                    }
                    st.session_state.reports_data.append(new_report)
                    st.success(f"✅ Отчет '{report_name}' успешно зарегистрирован!")
                else:
                    st.error("❌ Заполните все обязательные поля (отмечены *)")
    
    elif action == "Обновить существующий":
        st.subheader("🔄 Обновление существующего отчета")
        
        report_names = [f"{r['name']} (ID: {r['id']})" for r in st.session_state.reports_data]
        selected_report = st.selectbox("Выберите отчет для обновления:", report_names)
        
        if selected_report:
            report_id = int(selected_report.split("ID: ")[1].split(")")[0])
            report = next(r for r in st.session_state.reports_data if r['id'] == report_id)
            
            with st.form("update_report_form"):
                st.write(f"**Текущий статус:** {report['status']}")
                st.write(f"**Последнее обновление:** {report['last_update'].strftime('%d.%m.%Y')}")
                
                new_completion = st.slider("Процент завершенности", 0, 100, report['completion'])
                update_notes = st.text_area("Комментарии к обновлению")
                
                if st.form_submit_button("Обновить отчет"):
                    report['completion'] = new_completion
                    report['last_update'] = datetime.now()
                    if new_completion == 100:
                        report['status'] = 'Актуальный'
                    st.success("✅ Отчет успешно обновлен!")
                    st.rerun()
    
    elif action == "Сменить владельца":
        st.subheader("👤 Смена владельца отчета")
        
        report_names = [f"{r['name']} (Владелец: {r['owner']})" for r in st.session_state.reports_data]
        selected_report = st.selectbox("Выберите отчет:", report_names)
        
        if selected_report:
            new_owner = st.text_input("Новый владелец:")
            reason = st.text_area("Причина смены владельца:")
            
            if st.button("Сменить владельца"):
                if new_owner:
                    # Обновление владельца в данных
                    report_name = selected_report.split(" (Владелец:")[0]
                    for report in st.session_state.reports_data:
                        if report['name'] == report_name:
                            old_owner = report['owner']
                            report['owner'] = new_owner
                            break
                    
                    st.success(f"✅ Владелец изменен с {old_owner} на {new_owner}")
                else:
                    st.error("❌ Укажите нового владельца")
    
    elif action == "Автоматизировать":
        st.subheader("🤖 Автоматизация отчета")
        
        report_names = [r['name'] for r in st.session_state.reports_data]
        selected_report = st.selectbox("Выберите отчет для автоматизации:", report_names)
        
        if selected_report:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Источник данных")
                data_source = st.selectbox("Тип источника:", ["База данных", "API", "Файл Excel", "Google Sheets"])
                connection_string = st.text_input("Строка подключения:")
                
            with col2:
                st.markdown("#### Настройки автоматизации")
                auto_frequency = st.selectbox("Частота обновления:", ["Ежедневно", "Еженедельно", "Ежемесячно"])
                notification = st.checkbox("Уведомления о статусе")
                
            st.markdown("#### Сценарий обработки данных")
            processing_script = st.text_area("Python скрипт (опционально):", height=100)
            
            if st.button("Настроить автоматизацию"):
                st.success("✅ Автоматизация настроена! Отчет будет обновляться автоматически.")
                st.info("ℹ️ Первое автоматическое обновление запланировано на завтра.")

elif selected_page == "🏷️ Атрибуты и термины":
    st.title("🏷️ Формирование атрибутов и терминов")
    
    tab1, tab2 = st.tabs(["🔄 Конвертер шаблонов", "🧠 Подбор терминов ИИ"])
    
    with tab1:
        st.subheader("Конвертер шаблона COS в формат атрибутного состава")
        
        uploaded_file = st.file_uploader("Загрузите COS шаблон", type=['xlsx', 'xls', 'csv'])
        
        if uploaded_file is not None:
            st.success("✅ Файл загружен успешно!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Настройки конвертации")
                mapping_type = st.selectbox("Тип маппинга:", ["Автоматический", "Ручной", "Смешанный"])
                include_metadata = st.checkbox("Включить метаданные", value=True)
                validate_structure = st.checkbox("Валидировать структуру", value=True)
                
            with col2:
                st.markdown("#### Предварительный просмотр")
                st.info("Обнаружено 15 полей для конвертации")
                st.info("Типы данных: текст (8), числовые (5), даты (2)")
                
            if st.button("Конвертировать"):
                with st.spinner("Конвертация в процессе..."):
                    import time
                    time.sleep(2)
                
                st.success("✅ Конвертация завершена!")
                
                # Пример результата
                result_data = {
                    'Атрибут': ['Название', 'Департамент', 'Владелец', 'Дата создания', 'Статус'],
                    'Тип': ['Текст', 'Справочник', 'Пользователь', 'Дата', 'Перечисление'],
                    'Обязательный': [True, True, True, True, False],
                    'Описание': ['Название отчета', 'Подразделение', 'Ответственный', 'Дата создания', 'Текущий статус']
                }
                
                df_result = pd.DataFrame(result_data)
                st.dataframe(df_result, use_container_width=True)
                
                st.download_button(
                    label="Скачать атрибутный состав",
                    data=df_result.to_csv(index=False),
                    file_name="attributes_structure.csv",
                    mime="text/csv"
                )
    
    with tab2:
        st.subheader("ИИ-ассистент для подбора терминов")
        
        context_input = st.text_area(
            "Опишите контекст отчета или вставьте фрагмент текста:",
            height=100,
            placeholder="Например: Финансовый отчет содержит данные о выручке, расходах, прибыли..."
        )
        
        domain = st.selectbox("Предметная область:", ["Финансы", "Продажи", "HR", "ИТ", "Маркетинг", "Операции"])
        
        terminology_type = st.multiselect(
            "Типы терминов для подбора:",
            ["Ключевые понятия", "Синонимы", "Сокращения", "Переводы", "Связанные термины"]
        )
        
        if st.button("Сгенерировать термины"):
            if context_input:
                with st.spinner("ИИ анализирует контекст..."):
                    import time
                    time.sleep(2)
                
                st.success("✅ Термины сгенерированы!")
                
                # Имитация результата ИИ
                terms_data = {
                    'Термин': ['ROI', 'EBITDA', 'Cash Flow', 'Выручка', 'Маржинальность'],
                    'Определение': [
                        'Возврат на инвестиции',
                        'Прибыль до налогов и амортизации', 
                        'Денежный поток',
                        'Общий доход от продаж',
                        'Доля прибыли в выручке'
                    ],
                    'Синонимы': [
                        'Return on Investment',
                        'Операционная прибыль',
                        'Поток денежных средств', 
                        'Доходы, Sales',
                        'Рентабельность, Margin'
                    ],
                    'Категория': ['Финансы', 'Финансы', 'Финансы', 'Финансы', 'Финансы']
                }
                
                df_terms = pd.DataFrame(terms_data)
                st.dataframe(df_terms, use_container_width=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="Экспорт в Excel",
                        data="Термины (заглушка)",
                        file_name="generated_terms.xlsx",
                        mime="application/vnd.ms-excel"
                    )
                
                with col2:
                    if st.button("Добавить в глоссарий"):
                        st.success("✅ Термины добавлены в корпоративный глоссарий")
            else:
                st.error("❌ Введите контекст для анализа")

elif selected_page == "📈 Дашборд актуальности":
    st.title("📈 Дашборд актуальности отчетов")
    
    # Фильтры
    col1, col2, col3 = st.columns(3)
    
    with col1:
        departments = ['Все'] + list(set([r['department'] for r in st.session_state.reports_data]))
        selected_dept = st.selectbox("Департамент:", departments)
    
    with col2:
        status_filter = st.selectbox("Статус:", ['Все', 'Актуальный', 'Требует обновления', 'Новый'])
    
    with col3:
        date_range = st.selectbox("Период:", ['Все время', 'Последний месяц', 'Последняя неделя'])
    
    # Фильтрация данных
    filtered_data = st.session_state.reports_data
    if selected_dept != 'Все':
        filtered_data = [r for r in filtered_data if r['department'] == selected_dept]
    if status_filter != 'Все':
        filtered_data = [r for r in filtered_data if r['status'] == status_filter]
    
    # Метрики
    col1, col2, col3, col4 = st.columns(4)
    
    total_reports = len(filtered_data)
    actual_reports = len([r for r in filtered_data if r['status'] == 'Актуальный'])
    actual_percentage = (actual_reports / total_reports * 100) if total_reports > 0 else 0
    
    with col1:
        st.metric("Всего отчетов", total_reports)
    
    with col2:
        st.metric("Актуальных", actual_reports)
    
    with col3:
        st.metric("% Актуальности", f"{actual_percentage:.1f}%")
    
    with col4:
        overdue = len([r for r in filtered_data if r['next_update'] < datetime.now()])
        st.metric("Просрочено", overdue, delta=f"-{overdue}")
    
    # Графики
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Распределение по статусам")
        status_counts = {}
        for report in filtered_data:
            status = report['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        if status_counts:
            fig_pie = px.pie(
                values=list(status_counts.values()),
                names=list(status_counts.keys()),
                color_discrete_map={
                    'Актуальный': '#28a745',
                    'Требует обновления': '#ffc107', 
                    'Новый': '#17a2b8'
                }
            )
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.subheader("Процент завершенности")
        completion_data = [(r['name'], r['completion']) for r in filtered_data]
        if completion_data:
            names, completions = zip(*completion_data)
            
            fig_bar = px.bar(
                x=list(names),
                y=list(completions),
                color=list(completions),
                color_continuous_scale='RdYlGn',
                title="Завершенность отчетов (%)"
            )
            fig_bar.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_bar, use_container_width=True)
    
    # Детальная таблица
    st.subheader("Детализация по отчетам")
    
    if filtered_data:
        df_display = pd.DataFrame([
            {
                'Название': r['name'],
                'Департамент': r['department'], 
                'Владелец': r['owner'],
                'Статус': r['status'],
                'Завершенность': f"{r['completion']}%",
                'Последнее обновление': r['last_update'].strftime('%d.%m.%Y'),
                'Следующая актуализация': r['next_update'].strftime('%d.%m.%Y'),
                'Дней до обновления': (r['next_update'] - datetime.now()).days
            }
            for r in filtered_data
        ])
        
        # Стилизация таблицы
        def highlight_status(row):
            if row['Дней до обновления'] < 0:
                return ['background-color: #ffebee'] * len(row)
            elif row['Дней до обновления'] < 7:
                return ['background-color: #fff3e0'] * len(row)
            else:
                return [''] * len(row)
        
        styled_df = df_display.style.apply(highlight_status, axis=1)
        st.dataframe(styled_df, use_container_width=True)
        
        # Анализ проблем
        st.subheader("Анализ проблем и рекомендации")
        
        for report in filtered_data:
            if report['next_update'] < datetime.now() or report['completion'] < 100:
                with st.expander(f"⚠️ {report['name']} - требует внимания"):
                    issues = []
                    if report['next_update'] < datetime.now():
                        days_overdue = (datetime.now() - report['next_update']).days
                        issues.append(f"Просрочен на {days_overdue} дней")
                    
                    if report['completion'] < 100:
                        issues.append(f"Завершенность: {report['completion']}%")
                    
                    if report['status'] == 'Требует обновления':
                        issues.append("Требует актуализации данных")
                    
                    st.write("**Выявленные проблемы:**")
                    for issue in issues:
                        st.write(f"• {issue}")
                    
                    st.write(f"**Рекомендация:** Связаться с владельцем ({report['owner']}) для актуализации отчета")
                    st.write(f"**Дата следующей актуализации:** {report['next_update'].strftime('%d.%m.%Y')}")

elif selected_page == "🤖 Задать вопрос":
    st.title("🤖 ИИ-ассистент по отчетам")
    
    # История чата
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Привет! Я ИИ-ассистент системы управления отчетами. Чем могу помочь?"}
        ]
    
    # Отображение истории
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])
    
    # Поле ввода
    user_input = st.chat_input("Введите ваш вопрос...")
    
    if user_input:
        # Добавляем вопрос пользователя
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        
        # Генерируем ответ (имитация ИИ)
        response = generate_ai_response(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        
        st.rerun()
    
    # Боковая панель с частыми вопросами
    with st.sidebar:
        st.subheader("💡 Частые вопросы")
        
        frequent_questions = [
            "Как создать новый отчет?",
            "Как настроить автоматизацию?",
            "Кто может быть владельцем отчета?",
            "Как изменить статус отчета?",
            "Где найти шаблоны отчетов?"
        ]
        
        for question in frequent_questions:
            if st.button(question, key=f"faq_{question}"):
                st.session_state.chat_history.append({"role": "user", "content": question})
                response = generate_ai_response(question)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()

def generate_ai_response(question):
    """Генерация ответа ИИ-ассистента"""
    question_lower = question.lower()
    
    if "создать" in question_lower and "отчет" in question_lower:
        return """Для создания нового отчета:
1. Перейдите в раздел "Действия с отчетами"
2. Выберите "Зарегистрировать новый"
3. Заполните обязательные поля: название, департамент, владелец
4. Выберите тип отчета и периодичность обновления
5. Нажмите "Зарегистрировать отчет"

Не забудьте скачать подходящий шаблон из раздела "Инструкции по отчетам"!"""
    
    elif "автоматизац" in question_lower:
        return """Настройка автоматизации отчета:
1. Откройте "Действия с отчетами" → "Автоматизировать"
2. Выберите отчет для автоматизации
3. Укажите источник данных (БД, API, Excel файл)
4. Настройте частоту обновления
5. При необходимости добавьте скрипт обработки данных

Система будет автоматически обновлять отчет согласно расписанию."""
    
    elif "владелец" in question_lower:
        return """Владельцем отчета может быть:
- Любой сотрудник с доступом к необходимым данным
- Сотрудник, ответственный за актуальность информации
- Руководитель подразделения (для департаментских отчетов)

Для смены владельца используйте "Действия с отчетами" → "Сменить владельца"."""
    
    elif "статус" in question_lower:
        return """Статусы отчетов:
- **Новый**: только что созданный отчет
- **Актуальный**: отчет с актуальными данными
- **Требует обновления**: отчет нуждается в актуализации

Статус автоматически обновляется при изменении данных отчета."""
    
    elif "шаблон" in question_lower:
        return """Шаблоны отчетов находятся в разделе "Инструкции по отчетам" → вкладка "Шаблоны".
Доступны шаблоны для:
- Финансовых отчетов
- Отчетов по продажам  
- HR отчетов
- Операционных отчетов

Каждый шаблон содержит готовую структуру и рекомендации по заполнению."""
    
    else:
        return f"""Спасибо за вопрос! Я постараюсь помочь с "{question}".

Для получения более детальной информации рекомендую:
- Изучить раздел "Инструкции по отчетам"
- Обратиться к частым вопросам
- Связаться с администратором системы

Есть ли еще вопросы по работе с отчетами?"""

elif selected_page == "💬 Обратная связь":
    st.title("💬 Обратная связь")
    
    st.markdown("""
    ### Ваше мнение важно для нас!
    Помогите улучшить систему управления отчетами - поделитесь своими впечатлениями, предложениями или сообщите о проблемах.
    """)
    
    # Форма обратной связи
    with st.form("feedback_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            feedback_type = st.selectbox(
                "Тип обращения:",
                ["Предложение по улучшению", "Сообщение об ошибке", "Вопрос", "Благодарность", "Другое"]
            )
            
            priority = st.selectbox(
                "Приоритет:",
                ["Низкий", "Средний", "Высокий", "Критический"]
            )
        
        with col2:
            name = st.text_input("Ваше имя:")
            email = st.text_input("Email для связи:")
        
        subject = st.text_input("Тема сообщения:")
        message = st.text_area("Подробное описание:", height=150)
        
        # Дополнительные опции
        st.markdown("#### Дополнительные опции")
        col1, col2 = st.columns(2)
        
        with col1:
            attach_screenshot = st.checkbox("Прикрепить скриншот")
            anonymous = st.checkbox("Анонимное обращение")
        
        with col2:
            subscribe_updates = st.checkbox("Получать уведомления об обновлениях")
            
        # Файлы
        uploaded_files = st.file_uploader(
            "Прикрепить файлы (опционально):",
            accept_multiple_files=True,
            type=['png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx']
        )
        
        submit_feedback = st.form_submit_button("Отправить обратную связь")
        
        if submit_feedback:
            if subject and message:
                feedback_item = {
                    'id': len(st.session_state.feedback_data) + 1,
                    'type': feedback_type,
                    'priority': priority,
                    'name': name if not anonymous else "Анонимно",
                    'email': email,
                    'subject': subject,
                    'message': message,
                    'date': datetime.now(),
                    'status': 'Новое'
                }
                
                st.session_state.feedback_data.append(feedback_item)
                st.success("✅ Спасибо за обратную связь! Ваше сообщение принято и будет рассмотрено.")
                
                # Показать номер обращения
                st.info(f"📋 Номер вашего обращения: FB-{feedback_item['id']:04d}")
                
            else:
                st.error("❌ Заполните обязательные поля: тема и описание")
    
    # Статистика обратной связи
    if st.session_state.feedback_data:
        st.markdown("---")
        st.subheader("📊 Статистика обратной связи")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_feedback = len(st.session_state.feedback_data)
            st.metric("Всего обращений", total_feedback)
        
        with col2:
            recent_feedback = len([f for f in st.session_state.feedback_data 
                                 if (datetime.now() - f['date']).days <= 7])
            st.metric("За последнюю неделю", recent_feedback)
        
        with col3:
            avg_response_time = "2.5 дня"  # Заглушка
            st.metric("Среднее время ответа", avg_response_time)

# Админ страницы
elif selected_page == "🔍 Контроль публикации":
    st.title("🔍 Контроль публикации отчетов")
    
    # Фильтры для админа
    col1, col2, col3 = st.columns(3)
    
    with col1:
        status_filter = st.selectbox("Статус публикации:", 
                                   ["Все", "Ожидает модерации", "Одобрено", "Отклонено", "Опубликовано"])
    
    with col2:
        dept_filter = st.selectbox("Департамент:", 
                                 ["Все"] + list(set([r['department'] for r in st.session_state.reports_data])))
    
    with col3:
        date_filter = st.date_input("Дата создания от:")
    
    # Таблица отчетов для модерации
    st.subheader("Отчеты, ожидающие модерации")
    
    moderation_data = []
    for report in st.session_state.reports_data:
        moderation_data.append({
            'ID': report['id'],
            'Название': report['name'],
            'Автор': report['owner'],
            'Департамент': report['department'],
            'Дата создания': report['last_update'].strftime('%d.%m.%Y'),
            'Статус': 'Ожидает модерации',
            'Приоритет': random.choice(['Низкий', 'Средний', 'Высокий'])
        })
    
    df_moderation = pd.DataFrame(moderation_data)
    
    # Интерактивная таблица с действиями
    for idx, row in df_moderation.iterrows():
        with st.expander(f"📋 {row['Название']} - {row['Автор']}"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(f"**Департамент:** {row['Департамент']}")
                st.write(f"**Дата создания:** {row['Дата создания']}")
                st.write(f"**Приоритет:** {row['Приоритет']}")
                
                # Комментарий модератора
                moderator_comment = st.text_area(f"Комментарий модератора:", 
                                               key=f"comment_{row['ID']}")
            
            with col2:
                st.write("**Действия:**")
                
                if st.button("✅ Одобрить", key=f"approve_{row['ID']}"):
                    st.success("Отчет одобрен!")
                
                if st.button("❌ Отклонить", key=f"reject_{row['ID']}"):
                    st.error("Отчет отклонен!")
                
                if st.button("📝 Запросить правки", key=f"revise_{row['ID']}"):
                    st.warning("Запрошены правки!")

elif selected_page == "📊 Статистика публикации":
    st.title("📊 Статистика публикации отчетов")
    
    # Метрики
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Всего отчетов", len(st.session_state.reports_data))
    
    with col2:
        published = len([r for r in st.session_state.reports_data if r['status'] == 'Актуальный'])
        st.metric("Опубликовано", published)
    
    with col3:
        pending = len([r for r in st.session_state.reports_data if r['status'] == 'Новый'])
        st.metric("На модерации", pending)
    
    with col4:
        avg_time = "3.2 дня"  # Заглушка
        st.metric("Среднее время публикации", avg_time)
    
    # Графики статистики
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Публикации по департаментам")
        dept_counts = {}
        for report in st.session_state.reports_data:
            dept = report['department']
            dept_counts[dept] = dept_counts.get(dept, 0) + 1
        
        fig_dept = px.bar(
            x=list(dept_counts.keys()),
            y=list(dept_counts.values()),
            title="Количество отчетов по департаментам"
        )
        st.plotly_chart(fig_dept, use_container_width=True)
    
    with col2:
        st.subheader("Динамика публикаций")
        # Генерация данных для примера
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
        publications = [random.randint(5, 25) for _ in dates]
        
        fig_timeline = px.line(
            x=dates,
            y=publications,
            title="Публикации по месяцам"
        )
        st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Детальная аналитика
    st.subheader("Детальная аналитика")
    
    tab1, tab2, tab3 = st.tabs(["📈 Тренды", "⏱️ Время обработки", "👥 Активность пользователей"])
    
    with tab1:
        st.markdown("#### Тренды публикации")
        
        # Тренд по типам отчетов
        trend_data = {
            'Месяц': ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн'],
            'Финансовые': [12, 15, 10, 18, 20, 16],
            'Операционные': [8, 12, 15, 10, 14, 18],
            'Аналитические': [5, 8, 12, 15, 10, 12]
        }
        
        df_trend = pd.DataFrame(trend_data)
        
        fig_trend = px.line(
            df_trend,
            x='Месяц',
            y=['Финансовые', 'Операционные', 'Аналитические'],
            title="Тренды по типам отчетов"
        )
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with tab2:
        st.markdown("#### Время обработки отчетов")
        
        processing_data = {
            'Этап': ['Создание', 'Модерация', 'Правки', 'Публикация'],
            'Среднее время (дни)': [1.2, 2.5, 1.8, 0.5],
            'Медиана (дни)': [1.0, 2.0, 1.5, 0.3]
        }
        
        df_processing = pd.DataFrame(processing_data)
        
        fig_processing = px.bar(
            df_processing,
            x='Этап',
            y=['Среднее время (дни)', 'Медиана (дни)'],
            title="Время обработки по этапам",
            barmode='group'
        )
        st.plotly_chart(fig_processing, use_container_width=True)
    
    with tab3:
        st.markdown("#### Активность пользователей")
        
        # Топ авторов отчетов
        author_counts = {}
        for report in st.session_state.reports_data:
            author = report['owner']
            author_counts[author] = author_counts.get(author, 0) + 1
        
        top_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)
        
        st.markdown("**Топ авторов отчетов:**")
        for i, (author, count) in enumerate(top_authors[:5], 1):
            st.write(f"{i}. {author} - {count} отчетов")

elif selected_page == "⚠️ Проблемные вопросы":
    st.title("⚠️ Проблемные вопросы")
    
    st.markdown("""
    ### Отчеты, требующие особого внимания
    Здесь отображаются отчеты с выявленными проблемами и комментарии администраторов.
    """)
    
    # Список проблемных отчетов
    problematic_reports = []
    for report in st.session_state.reports_data:
        issues = []
        if report['next_update'] < datetime.now():
            issues.append("Просрочен")
        if report['completion'] < 80:
            issues.append("Низкая завершенность")
        if report['status'] == 'Требует обновления':
            issues.append("Требует актуализации")
        
        if issues:
            problematic_reports.append({
                'report': report,
                'issues': issues
            })
    
    if not problematic_reports:
        st.success("🎉 Отлично! Проблемных отчетов не найдено.")
    else:
        for item in problematic_reports:
            report = item['report']
            issues = item['issues']
            
            with st.expander(f"⚠️ {report['name']} - {len(issues)} проблем(ы)"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Владелец:** {report['owner']}")
                    st.write(f"**Департамент:** {report['department']}")
                    st.write(f"**Статус:** {report['status']}")
                    st.write(f"**Завершенность:** {report['completion']}%")
                    
                    st.write("**Выявленные проблемы:**")
                    for issue in issues:
                        st.write(f"• {issue}")
                
                with col2:
                    st.write("**Информация:**")
                    days_overdue = (datetime.now() - report['next_update']).days
                    if days_overdue > 0:
                        st.error(f"Просрочен на {days_overdue} дней")
                    
                    st.write(f"**Последнее обновление:**")
                    st.write(report['last_update'].strftime('%d.%m.%Y'))
                
                # Комментарии администратора
                st.markdown("#### Комментарии администратора")
                
                admin_comment = st.text_area(
                    "Комментарий:",
                    key=f"admin_comment_{report['id']}",
                    placeholder="Добавьте комментарий о проблеме и планах решения..."
                )
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("📧 Уведомить владельца", key=f"notify_{report['id']}"):
                        st.success("Владелец уведомлен!")
                
                with col2:
                    if st.button("🔄 Принудительное обновление", key=f"force_update_{report['id']}"):
                        st.warning("Запущено принудительное обновление")
                
                with col3:
                    if st.button("🚫 Заблокировать отчет", key=f"block_{report['id']}"):
                        st.error("Отчет заблокирован")
                
                # История действий
                with st.expander("📝 История действий"):
                    st.write("- 15.05.2024: Создан отчет")
                    st.write("- 20.05.2024: Первое обновление") 
                    st.write("- 01.06.2024: Уведомление о необходимости актуализации")
                    st.write("- 10.06.2024: Отчет помечен как проблемный")

# Дополнительные функции
def generate_ai_response(question):
    """Генерация ответа ИИ-ассистента"""
    question_lower = question.lower()
    
    if "создать" in question_lower and "отчет" in question_lower:
        return """Для создания нового отчета:
1. Перейдите в раздел "Действия с отчетами"
2. Выберите "Зарегистрировать новый"
3. Заполните обязательные поля: название, департамент, владелец
4. Выберите тип отчета и периодичность обновления
5. Нажмите "Зарегистрировать отчет"

Не забудьте скачать подходящий шаблон из раздела "Инструкции по отчетам"!"""
    
    elif "автоматизац" in question_lower:
        return """Настройка автоматизации отчета:
1. Откройте "Действия с отчетами" → "Автоматизировать"
2. Выберите отчет для автоматизации
3. Укажите источник данных (БД, API, Excel файл)
4. Настройте частоту обновления
5. При необходимости добавьте скрипт обработки данных

Система будет автоматически обновлять отчет согласно расписанию."""
    
    elif "владелец" in question_lower:
        return """Владельцем отчета может быть:
- Любой сотрудник с доступом к необходимым данным
- Сотрудник, ответственный за актуальность информации
- Руководитель подразделения (для департаментских отчетов)

Для смены владельца используйте "Действия с отчетами" → "Сменить владельца"."""
    
    elif "статус" in question_lower:
        return """Статусы отчетов:
- **Новый**: только что созданный отчет
- **Актуальный**: отчет с актуальными данными
- **Требует обновления**: отчет нуждается в актуализации

Статус автоматически обновляется при изменении данных отчета."""
    
    elif "шаблон" in question_lower:
        return """Шаблоны отчетов находятся в разделе "Инструкции по отчетам" → вкладка "Шаблоны".
Доступны шаблоны для:
- Финансовых отчетов
- Отчетов по продажам  
- HR отчетов
- Операционных отчетов

Каждый шаблон содержит готовую структуру и рекомендации по заполнению."""
    
    else:
        return f"""Спасибо за вопрос! Я постараюсь помочь с "{question}".

Для получения более детальной информации рекомендую:
- Изучить раздел "Инструкции по отчетам"
- Обратиться к частым вопросам
- Связаться с администратором системы

Есть ли еще вопросы по работе с отчетами?"""

# Футер
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8em;'>
    © 2024 Система управления отчетами | Версия 1.0 | 
    <a href='#'>Техподдержка</a> | 
    <a href='#'>Документация</a>
</div>
""", unsafe_allow_html=True)