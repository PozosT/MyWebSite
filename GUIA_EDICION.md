# 📝 Guía de Edición - Sitio Web Académico

## 🎯 ¿Qué puedes editar fácilmente?

### 1. 📚 **PUBLICACIONES** - Archivo: `_data/publist.yml`

**¿Qué editar?** Lista de todas tus publicaciones académicas.

**Formato de cada publicación:**
```yaml
- title: "Título de la publicación"
  authors: "Autores separados por comas"
  url: "nombre-del-archivo-sin-extension"
  image: "nombre-del-archivo.jpg"
  display: "Revista/Conferencia donde se publicó"
  year: 2024
  abstract: "Resumen de la publicación"
```

**Ejemplo:**
```yaml
- title: "Optimal Planning of Distribution Systems"
  authors: "Tabares, Alejandra; Franco, John F; Lavorato, Marina"
  url: "tabares2024optimal"
  image: "tabares2024optimal.jpg"
  display: "IEEE Transactions on Power Systems"
  year: 2024
  abstract: "This paper presents a novel approach for optimal planning..."
```

**⚠️ IMPORTANTE:**
- El `url` debe coincidir con el nombre del archivo en `_publications/` (sin extensión)
- Debes tener el archivo correspondiente en `_publications/` (ej: `tabares2024optimal.md`)
- Las publicaciones se ordenan automáticamente por año (más recientes primero)

---

### 2. 👥 **EQUIPO** - Archivo: `_data/team_members.yml`

**¿Qué editar?** Información de estudiantes, postdocs y colaboradores.

**Formato de cada miembro:**
```yaml
- name: "Nombre completo"
  photo: "nombre-foto.jpg"
  info: "Cargo actual, fecha de inicio"
  email: "email@institucion.edu"
  website: "https://sitio-web.com"
  number_educ: 2
  education1: "Ph.D. con <a href='link'>Profesor</a>, Universidad"
  education2: "M.Sc. con <a href='link'>Profesor</a>, Universidad"
```

**Ejemplo:**
```yaml
- name: "María González"
  photo: "maria_gonzalez.jpg"
  info: "Ph.D. Student, started Jan 2024"
  email: "m.gonzalez@uniandes.edu.co"
  website: "https://mariagonzalez.com"
  number_educ: 1
  education1: "M.Sc. con <a href='https://profesor.edu'>Dr. García</a>, Universidad de los Andes"
```

**⚠️ IMPORTANTE:**
- La foto debe estar en `images/team/`
- `number_educ` indica cuántas líneas de educación mostrar (1-4)
- Usa HTML para enlaces en `education1`, `education2`, etc.

---

### 3. 📖 **CURSOS** - Carpeta: `_courses/`

**¿Qué editar?** Información de cursos que impartes.

**Estructura:**
- Cada curso tiene su archivo `.md` (ej: `HEUR-2025.md`)
- También puede tener un PDF del syllabus (ej: `HEUR-2025.pdf`)

**Formato del archivo `.md`:**
```yaml
---
title: "Nombre del Curso"
layout: course
sitemap: false
name: "Nombre completo del curso"
name_url: "https://link-al-curso"
year_start: 2025
year_end: 
institution: "Universidad de los Andes"
type: "msc"  # msc, phd, undergrad
type: "introductory-intermediate"  # nivel
students: "35+"
code: "HEUR-2025"
subheading: "Descripción breve del curso"
pdf: "nombre-del-pdf-sin-extension"
comment: "Comentarios adicionales"
---
```

**Contenido del curso:**
- Introducción
- Tu rol
- Objetivos de aprendizaje
- Material de estudio
- Organización y cronograma
- Evaluación
- Temas y cronograma
- Reglas y políticas
- Resultados esperados

---

### 4. 🔬 **INVESTIGACIONES** - Archivo: `research.md`

**¿Qué editar?** Página principal de investigación.

**Ubicación:** `research.md` (en la raíz del sitio)

**Estructura típica:**
```markdown
---
title: Research
permalink: /research/
---

## Research Areas

### Area 1: [Nombre del área]
Descripción de la línea de investigación...

### Area 2: [Nombre del área]
Descripción de la línea de investigación...

## Current Projects

### Project 1: [Nombre del proyecto]
- **Funding:** [Fuente de financiación]
- **Duration:** [Período]
- **Description:** [Descripción breve]

## Collaborations

- **Institution 1:** [Descripción de la colaboración]
- **Institution 2:** [Descripción de la colaboración]
```

---

## 🚀 **Cómo hacer cambios**

### Paso 1: Editar el archivo
1. Abre el archivo correspondiente en tu editor
2. Haz los cambios siguiendo el formato
3. Guarda el archivo

### Paso 2: Subir los cambios
```bash
git add .
git commit -m "Actualizar [tipo de contenido]: [descripción breve]"
git push
```

### Paso 3: Verificar
- Espera 2-3 minutos para que GitHub Pages se actualice
- Visita tu sitio: `https://[usuario].github.io/MyWebSite/`
- Limpia la caché del navegador si no ves los cambios

---

## 📁 **Estructura de archivos**

```
MyWebSite/
├── _data/
│   ├── publist.yml          ← PUBLICACIONES
│   └── team_members.yml     ← EQUIPO
├── _courses/
│   ├── HEUR-2025.md         ← CURSOS
│   ├── MEL-2025.md
│   └── [otros cursos].md
├── _publications/
│   ├── tabares2024optimal.md ← ARCHIVOS DE PUBLICACIONES
│   └── [otros papers].md
├── images/
│   ├── team/                ← FOTOS DEL EQUIPO
│   └── research/            ← IMÁGENES DE INVESTIGACIÓN
├── research.md              ← PÁGINA DE INVESTIGACIÓN
└── index.md                 ← PÁGINA PRINCIPAL
```

---

## ⚠️ **Archivos que NO debes tocar**

❌ **Nunca edites estos archivos:**
- `_config.yml` (configuración del sitio)
- `_layouts/` (plantillas de diseño)
- `_includes/` (componentes reutilizables)
- `_sass/` (estilos CSS)
- `js/` (JavaScript)
- `css/` (hojas de estilo)

✅ **Solo edita estos archivos:**
- `_data/publist.yml` (publicaciones)
- `_data/team_members.yml` (equipo)
- `_courses/*.md` (cursos)
- `research.md` (investigación)
- `index.md` (página principal - solo si es necesario)

---

## 🔧 **Solución de problemas**

### ¿Los cambios no aparecen?
1. **Limpia la caché del navegador** (Ctrl+F5)
2. **Espera 5 minutos** para que GitHub Pages se actualice
3. **Verifica que hiciste commit y push**

### ¿Error de formato?
1. **Revisa la indentación** (usa espacios, no tabs)
2. **Verifica las comillas** (usa comillas dobles `"`)
3. **Asegúrate de que el formato YAML sea correcto**

### ¿No encuentras un archivo?
1. **Busca en la carpeta correcta** según la guía
2. **Verifica el nombre exacto** del archivo
3. **Crea el archivo si no existe** siguiendo el formato

---

## 📞 **¿Necesitas ayuda?**

Si algo no funciona o tienes dudas:
1. **Revisa esta guía** primero
2. **Verifica el formato** de los archivos
3. **Limpia la caché** del navegador
4. **Espera** a que GitHub Pages se actualice

¡Con esta guía deberías poder actualizar tu sitio web sin problemas técnicos!
