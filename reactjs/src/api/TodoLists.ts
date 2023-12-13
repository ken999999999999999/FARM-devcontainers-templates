import { useMutation, useQuery } from "react-query"
import { apiClient } from "./common"

const todoLists = "/todo-lists/"

interface ICreateTodoListCommand {
  title: string
}

interface IUpdateTodoListCommand {
  id: string
  title: string
}

export const useGetTodoList = () =>
  useQuery(["todoList", "getList"], () => apiClient.get(todoLists))

export const useCreateTodoList = () =>
  useMutation({
    mutationKey: ["todoList", "create"],
    mutationFn: (command: ICreateTodoListCommand) =>
      apiClient.post(todoLists, command),
  })

export const useUpdateTodoList = () =>
  useMutation({
    mutationKey: ["todoList", "update"],
    mutationFn: (command: IUpdateTodoListCommand) =>
      apiClient.put(todoLists + command.id, command),
  })
