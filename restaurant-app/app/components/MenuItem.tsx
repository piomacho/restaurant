"use client";

export const MenuItem = ({
  id,
  name,
  price,
  onEdit,
  onDelete,
}: {
  id: string;
  name: string;
  price: number;
  onEdit: () => void;
  onDelete: (id: string) => void;
}) => {
  async function deleteMenu(id: string) {
    const res = await fetch(`http://127.0.0.1:8000/api/menu/${id}/`, {
      method: "DELETE",
    });
    if (!res.ok) {
      throw new Error("Failed to retrieve menu");
    }
    return Promise.resolve();
  }
  return (
    <div className="menu-item" data-id={id}>
      <div className="menu-item-info">
        <div className="menu-item-name">{name}</div>
        <div className="menu-item-price">${price.toFixed(2)}</div>
      </div>
      <div className="menu-item-actions">
        <button className="edit-button" onClick={onEdit}>
          Edit
        </button>
        <button
          className="delete-button"
          onClick={() => {
            deleteMenu(id).then(() => onDelete(id));
          }}
        >
          Delete
        </button>
      </div>
    </div>
  );
};
