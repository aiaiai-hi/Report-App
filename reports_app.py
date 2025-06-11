import streamlit as st
import pandas as pd
from datetime import datetime

# Конфигурация страницы
st.set_page_config(
    page_title="Система управления отчетами",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Инициализация состояния сессии
if 'admin_mode' not in st.session_state:
    st.session_state.admin_mode = False

# CSS стили для улучшения внешнего вида
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .page-header {
        font-size: 2rem;
        font-weight: bold;
        color: #333;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .sidebar-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .admin-badge {
        background-color: #ff4b4b;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 0.3rem;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .coming-soon {
        text-align: center;
        color: #666;
        font-style: italic;
        font-size: 1.2rem;
        margin-top: 3rem;
        padding: 2rem;
        border: 2px dashed #ccc;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок приложения
st.markdown('<div class="main-header">📊 Система управления отчетами</div>', unsafe_allow_html=True)

# Боковая панель с навигацией
with st.sidebar:
    st.markdown('<div class="sidebar-header">🧭 Навигация</div>', unsafe_allow_html=True)
    
    # Основное меню
    st.markdown("**Основные функции:**")
    main_pages = {
        "📋 Инструкции по отчетам": "instructions",
        "⚡ Действия с отчетами": "actions", 
        "🏷️ Сформировать атрибуты и термины": "attributes",
        "📈 Дашборд по актуальности отчетов": "dashboard",
        "🤖 Задать вопрос (ИИ ассистент)": "ai_assistant",
        "💬 Оставить обратную связь": "feedback"
    }
    
    # Для основного меню:
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "📋 Инструкции по отчетам"
    
    for page_name in main_pages.keys():
        if st.button(page_name, key=f"btn_{main_pages[page_name]}", use_container_width=True):
            st.session_state.selected_page = page_name
    
    st.markdown("---")
    
    # Админ панель
    st.markdown("**Административная панель:**")
    admin_toggle = st.checkbox("🔐 Режим администратора", key="admin_toggle")
    st.session_state.admin_mode = admin_toggle
    
    if st.session_state.admin_mode:
        st.markdown('<span class="admin-badge">АДМИН РЕЖИМ</span>', unsafe_allow_html=True)
        st.markdown("")
        
        admin_pages = {
            "🔍 Контроль публикации отчетов": "admin_control",
            "📊 Статистика по публикации": "admin_stats", 
            "⚠️ Проблемные вопросы": "admin_issues"
        }
        
        # Для админ меню:
        if 'selected_admin_page' not in st.session_state:
            st.session_state.selected_admin_page = "🔍 Контроль публикации отчетов"
            
        for page_name in admin_pages.keys():
            if st.button(page_name, key=f"admin_btn_{admin_pages[page_name]}", use_container_width=True):
                st.session_state.selected_admin_page = page_name
    
    # Информация о системе
    st.markdown("---")
    st.markdown("**ℹ️ Информация о системе**")
    st.caption(f"Время: {datetime.now().strftime('%H:%M:%S')}")
    st.caption("Версия: 1.0.0")

# Функции для отображения страниц
def show_instructions():
    st.markdown('<div class="page-header">📋 Инструкции по отчетам</div>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Здесь будут размещены подробные инструкции по работе с отчетами</div>', unsafe_allow_html=True)

def show_actions():
    st.markdown('<div class="page-header">⚡ Действия с отчетами</div>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Здесь будут доступны различные действия с отчетами: создание, редактирование, удаление</div>', unsafe_allow_html=True)

def show_attributes():
    st.markdown('<div class="page-header">🏷️ Сформировать атрибуты и термины</div>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Здесь будет возможность создавать и управлять атрибутами и терминами для отчетов</div>', unsafe_allow_html=True)

def show_dashboard():
    st.markdown('<div class="page-header">📈 Дашборд по актуальности отчетов</div>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Здесь будут отображаться графики и метрики актуальности отчетов</div>', unsafe_allow_html=True)

def show_ai_assistant():
    st.markdown('<div class="page-header">🤖 Задать вопрос (ИИ ассистент)</div>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Здесь будет интеграция с ИИ-ассистентом для ответов на вопросы</div>', unsafe_allow_html=True)

def show_feedback():
    st.markdown('<div class="page-header">💬 Оставить обратную связь</div>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Здесь будет форма для отправки обратной связи и предложений</div>', unsafe_allow_html=True)

def show_admin_control():
    st.markdown('<div class="page-header">🔍 Контроль публикации отчетов</div>', unsafe_allow_html=True)
    st.markdown('<span class="admin-badge">АДМИН</span>', unsafe_allow_html=True)
    
    from utils import display_request_analysis
    
    st.markdown("## 📊 Анализатор запросов и стадий рассмотрения")
    st.info("Загрузите файл с запросами для анализа времени рассмотрения и текущих стадий")
    
    display_request_analysis()

def show_admin_stats():
    st.markdown('<div class="page-header">📊 Статистика по публикации</div>', unsafe_allow_html=True)
    st.markdown('<span class="admin-badge">АДМИН</span>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Административная статистика и аналитика по публикациям</div>', unsafe_allow_html=True)

def show_admin_issues():
    st.markdown('<div class="page-header">⚠️ Проблемные вопросы</div>', unsafe_allow_html=True)
    st.markdown('<span class="admin-badge">АДМИН</span>', unsafe_allow_html=True)
    st.markdown('<div class="coming-soon">🚧 Мониторинг и управление проблемными вопросами</div>', unsafe_allow_html=True)

# Отображение выбранной страницы
if st.session_state.admin_mode and 'selected_admin_page' in st.session_state:
    # Показываем админ страницы
    page_map = {
        "🔍 Контроль публикации отчетов": show_admin_control,
        "📊 Статистика по публикации": show_admin_stats, 
        "⚠️ Проблемные вопросы": show_admin_issues
    }
    page_map[st.session_state.selected_admin_page]()
else:
    # Показываем основные страницы
    page_map = {
        "📋 Инструкции по отчетам": show_instructions,
        "⚡ Действия с отчетами": show_actions,
        "🏷️ Сформировать атрибуты и термины": show_attributes,
        "📈 Дашборд по актуальности отчетов": show_dashboard,
        "🤖 Задать вопрос (ИИ ассистент)": show_ai_assistant,
        "💬 Оставить обратную связь": show_feedback
    }
    page_map[st.session_state.selected_page]()

# Подвал приложения
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🏢 Компания XYZ")
with col2:
    st.caption("📧 support@company.com")
with col3:
    st.caption("📞 +7 (xxx) xxx-xx-xx")
