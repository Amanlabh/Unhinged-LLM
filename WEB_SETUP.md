# Cyber Fellow Web UI - Quick Start

## What's Been Created

A complete Next.js web application with:

✅ **ChatGPT-like Interface**
- Modern, clean chat UI
- Real-time message streaming
- Sidebar with conversation history
- Message bubbles with markdown support

✅ **User Management with Supabase**
- Email/password authentication
- User sessions
- Secure API routes
- Row-level security policies

✅ **Ollama Integration**
- Direct connection to local Ollama instance
- Streaming responses
- Conversation history
- Mistral model support

✅ **Database Schema**
- Conversations table
- Messages table
- User relationships
- Automatic cleanup on delete

## Quick Setup

### 1. Install Dependencies

```bash
cd web
npm install
```

### 2. Set Up Supabase

1. Go to [supabase.com](https://supabase.com) and create a project
2. Copy your project URL and anon key
3. Create `web/.env.local`:

```env
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
```

### 3. Create Database Tables

In Supabase SQL Editor, run the SQL from `web/SUPABASE_SETUP.md`

### 4. Make Sure Ollama is Running

```bash
ollama serve
```

Verify mistral model is available:
```bash
ollama list
```

### 5. Start the App

```bash
cd web
npm run dev
```

Visit `http://localhost:3000` and sign up!

## Project Structure

```
cyber-fellow/
├── web/                    # Next.js application
│   ├── app/               # App router pages
│   │   ├── api/          # API routes
│   │   ├── chat/         # Main chat interface
│   │   └── login/        # Auth page
│   ├── components/       # React components
│   ├── lib/              # Utilities
│   └── types/            # TypeScript types
└── [Python files]         # Original CLI assistant
```

## Features

### Authentication
- Sign up with email/password
- Sign in
- Protected routes
- Session management

### Chat Interface
- Real-time streaming responses
- Markdown rendering
- Conversation history
- Multiple conversations
- Delete conversations

### API Integration
- `/api/chat` - Send messages to Ollama
- `/api/conversations` - Manage conversations
- `/api/conversations/[id]` - Get/delete conversations
- `/api/conversations/[id]/messages` - Get messages

## Environment Variables

Required in `web/.env.local`:
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`

Optional:
- `OLLAMA_BASE_URL` (default: http://localhost:11434)
- `OLLAMA_MODEL` (default: mistral)

## Troubleshooting

**Can't connect to Ollama?**
- Make sure `ollama serve` is running
- Check `OLLAMA_BASE_URL` in environment

**Supabase errors?**
- Verify environment variables
- Check database tables are created
- Review RLS policies

**Authentication not working?**
- Check Supabase Auth settings
- Verify email confirmation settings
- Check browser console for errors

## Next Steps

1. Customize the UI styling
2. Add more features (export chats, search, etc.)
3. Deploy to Vercel/Netlify
4. Add more models support
5. Implement rate limiting
6. Add user profiles

Enjoy your Cyber Fellow web interface! 🛡️




