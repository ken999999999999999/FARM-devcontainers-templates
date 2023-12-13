import { useMutation } from "react-query"
import { apiClient } from "./common"

const todoItems = "/todo-items/"

interface ICreateTodoItemCommand {
  title: string
  todo_list_id: string
}

interface IUpdateTodoItemCommand {
  id: string
  is_done: boolean
}

export const useCreateTodoItem = () =>
  useMutation({
    mutationKey: ["todoItem", "create"],
    mutationFn: (command: ICreateTodoItemCommand) =>
      apiClient.post(todoItems, command),
  })

export const useUpdateTodoItem = () =>
  useMutation({
    mutationKey: ["todoItem", "update"],
    mutationFn: (command: IUpdateTodoItemCommand) =>
      apiClient.put(todoItems + command.id, command),
  })
