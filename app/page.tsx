"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Loader2, Send, Brain, CheckCircle2, XCircle } from "lucide-react"

export default function Home() {
  const [apiUrl, setApiUrl] = useState("http://localhost:5000")
  const [question, setQuestion] = useState("")
  const [answer, setAnswer] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [serverStatus, setServerStatus] = useState<"unknown" | "healthy" | "error">("unknown")

  const checkHealth = async () => {
    try {
      const response = await fetch(`${apiUrl}/health`)
      const data = await response.json()

      if (data.status === "healthy") {
        setServerStatus("healthy")
        setError("")
      } else {
        setServerStatus("error")
        setError("Server is not healthy")
      }
    } catch (err) {
      setServerStatus("error")
      setError("Cannot connect to server. Make sure it is running.")
    }
  }

  const askQuestion = async () => {
    if (!question.trim()) {
      setError("Please enter a question")
      return
    }

    setLoading(true)
    setError("")
    setAnswer("")

    try {
      const response = await fetch(`${apiUrl}/ask`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      })

      const data = await response.json()

      if (data.success) {
        setAnswer(data.answer)
      } else {
        setError(data.error || "Failed to get answer")
      }
    } catch (err) {
      setError("Failed to connect to API. Check your API URL.")
    } finally {
      setLoading(false)
    }
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      askQuestion()
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Brain className="w-12 h-12 text-blue-600" />
            <h1 className="text-4xl font-bold text-gray-900">ExamSathi AI</h1>
          </div>
          <p className="text-lg text-gray-600">Your Personal Educational AI Assistant</p>
        </div>

        {/* API Configuration */}
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>API Configuration</CardTitle>
            <CardDescription>Connect to your ExamSathi AI server</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex gap-3">
              <div className="flex-1">
                <Label htmlFor="api-url">API URL</Label>
                <Input
                  id="api-url"
                  value={apiUrl}
                  onChange={(e) => setApiUrl(e.target.value)}
                  placeholder="http://localhost:5000"
                  className="mt-1"
                />
              </div>
              <div className="flex items-end">
                <Button onClick={checkHealth} variant="outline">
                  Check Status
                </Button>
              </div>
            </div>

            {serverStatus !== "unknown" && (
              <div className="mt-3 flex items-center gap-2">
                {serverStatus === "healthy" ? (
                  <>
                    <CheckCircle2 className="w-5 h-5 text-green-600" />
                    <span className="text-sm text-green-600 font-medium">Server is healthy and ready</span>
                  </>
                ) : (
                  <>
                    <XCircle className="w-5 h-5 text-red-600" />
                    <span className="text-sm text-red-600 font-medium">Server is not responding</span>
                  </>
                )}
              </div>
            )}
          </CardContent>
        </Card>

        {/* Question Input */}
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>Ask a Question</CardTitle>
            <CardDescription>Enter your educational question below</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <Label htmlFor="question">Question</Label>
                <Textarea
                  id="question"
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  onKeyPress={handleKeyPress}
                  placeholder="What is photosynthesis?"
                  className="mt-1 min-h-[100px]"
                  disabled={loading}
                />
              </div>

              <Button onClick={askQuestion} disabled={loading || !question.trim()} className="w-full" size="lg">
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                    Thinking...
                  </>
                ) : (
                  <>
                    <Send className="w-4 h-4 mr-2" />
                    Get Answer
                  </>
                )}
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Error Display */}
        {error && (
          <Card className="mb-6 border-red-200 bg-red-50">
            <CardContent className="pt-6">
              <div className="flex items-start gap-3">
                <XCircle className="w-5 h-5 text-red-600 mt-0.5" />
                <div>
                  <p className="font-medium text-red-900">Error</p>
                  <p className="text-sm text-red-700">{error}</p>
                </div>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Answer Display */}
        {answer && (
          <Card className="border-green-200 bg-green-50">
            <CardHeader>
              <CardTitle className="text-green-900">Answer</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-gray-800 whitespace-pre-wrap leading-relaxed">{answer}</p>
            </CardContent>
          </Card>
        )}

        {/* Sample Questions */}
        <Card className="mt-6">
          <CardHeader>
            <CardTitle>Sample Questions</CardTitle>
            <CardDescription>Try these example questions</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid gap-2">
              {[
                "What is photosynthesis?",
                "Explain Newton's First Law of Motion",
                "What is the Pythagorean theorem?",
                "Define mitosis",
                "What is the water cycle?",
              ].map((sampleQ) => (
                <Button
                  key={sampleQ}
                  variant="outline"
                  className="justify-start text-left h-auto py-3 bg-transparent"
                  onClick={() => setQuestion(sampleQ)}
                  disabled={loading}
                >
                  {sampleQ}
                </Button>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Footer */}
        <div className="mt-8 text-center text-sm text-gray-500">
          <p>Built with ExamSathi AI - Your own educational model</p>
        </div>
      </div>
    </div>
  )
}
