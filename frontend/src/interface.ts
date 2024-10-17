export interface ArticleType{
    category: Category,
    id: number,
    title: string,
    text: string,
    articleImg: string,
    createdAt: string,
  }

export interface User{
  id: number,
  name: string,
  email: string,
  dob: Date,
  profileImg: string,
  createdAt: string,
  category: string,
}

export interface Category{
  id: number,
  category: string,
  image: HTMLImageElement
}
export interface Comment{
  user: User,
  article: ArticleType
}