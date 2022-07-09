export const useApiFetch = async (path) => {
    return await useFetch(() => `http://localhost:8000/api/v1/${path}`)
  }